import os
import warnings
from datetime import datetime
import base64
import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from Utils import utils
from allure_commons.types import AttachmentType
import allure



def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")



@pytest.fixture(scope="class")
def test_setup(request):
    browser = request.config.getoption("--browser")
    allure.dynamic.parameter("Browser", browser)
    driver = None

    if browser == "chrome":
        options = Options()
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("excludeSwitches", ['enable-automation'])
        options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        })
        driver = webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = FirefoxOptions()
        driver = webdriver.Firefox(options=options)

    warnings.simplefilter('ignore', ResourceWarning)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(utils.URL)
    request.cls.driver = driver
    yield
    driver.quit()



#@pytest.mark.hookwrapper
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call':
        extra.append(pytest_html.extras.url("https://practicesoftwaretesting.com/"))

        xfail = hasattr(report, 'wasxfail')

        if (report.skipped and xfail) or (report.failed and not xfail):
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_name = f"{report.nodeid.replace('::', '_')}_{timestamp}.png"

            # Capturar screenshot
            screenshot = item.cls.driver.get_screenshot_as_png()

            # Guardar imagen en Reports
            _capture_screenshot(screenshot, screenshot_name)

            # Adjuntar a Allure
            allure.attach(
                screenshot,
                name="Screenshot",
                attachment_type=AttachmentType.PNG
            )

            # Adjuntar a pytest-html
            screenshot_base64 = base64.b64encode(screenshot).decode("utf-8")

            extra.append(
                pytest_html.extras.png(screenshot_base64, name="Screenshot")
            )

        report.extras = extra


def _capture_screenshot(screenshot, name):
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    reports_path = os.path.join(project_root, "Reports")
    os.makedirs(reports_path, exist_ok=True)
    name = name.replace("/", "_").replace("\\", "_")
    final_path = os.path.join(reports_path, name)
    with open(final_path, "wb") as file:
        file.write(screenshot)
    return final_path



