import os
import warnings
from datetime import datetime

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

    if report.when == 'call' or report.when == 'setup':
        extra.append(pytest_html.extras.url("https://practicesoftwaretesting.com/"))
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  # <-- ahora funciona
            screenshot_name = f"{report.nodeid.replace('::', '_')}_{timestamp}.png"
            screenshot_path = _capture_screenshot(item.cls.driver, screenshot_name)

            # Adjunta a Allure
            allure.attach(item.cls.driver.get_screenshot_as_png(),
                          name="Screenshot",
                          attachment_type=AttachmentType.PNG)

            if screenshot_path:
                html = f'<div><img src="{screenshot_path}" alt="screenshot" style="width:304px;height:228px;" ' \
                       f'onclick="window.open(this.src)" align="right"/></div>'
                extra.append(pytest_html.extras.html(html))
        report.extras = extra


def _capture_screenshot(driver, name):
    reports_path = os.path.join("..", "Test", "Reports")
    os.makedirs(reports_path, exist_ok=True)
    final_path = os.path.join(reports_path, name)
    driver.get_screenshot_as_file(final_path)
    return final_path



