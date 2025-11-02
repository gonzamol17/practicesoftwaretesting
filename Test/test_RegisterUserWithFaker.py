import json
import time
from datetime import date

from selenium.webdriver.common.by import By

from POM.HeaderMenuPage import HeaderMenuPage
from POM.HomePage import HomePage
from POM.LoginPage import LoginPage
from POM.RegistrationPage import RegistrationPage
from Utils.BaseClass import BaseClass
from faker import Faker


class TestRegisterUserWithFaker(BaseClass):

      def test_RegisterUserWithFaker(self):
        log = self.get_Logger()
        fake = Faker()

        today = date.today()
        #start_date = today.replace(year=today.year - 40)  # fecha hace 40 años
        #end_date = today.replace(year=today.year - 15)  # fecha hace 18 años
        # Generar fecha de nacimiento dentro del rango
        birthdate = fake.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=40)
        # Formatear la fecha de nacimiento
        formatted_date = birthdate.strftime("%Y-%m-%d")
        #formatted_date = birthdate.strftime("%d/%m/%Y")

        log.info("Se está por loguear en la página")
        driver = self.driver
        hmp = HeaderMenuPage(driver)
        time.sleep(3)
        hmp.selectLinkSignIn()
        lp = LoginPage(driver)
        lp.selectRegisterLinkOption()
        rp = RegistrationPage(driver)
        file1 = open("..\\Data\\Register.json", "r")
        jsondata1 = file1.read()
        obj1 = json.loads(jsondata1)
        list1 = obj1['users']
        n = 0
        # rp.completeRegisterForm(fake.name(), fake.last_name(), fake.date_of_birth().strftime("%d/%m/%Y"), list1[n].get("address"),
        #                       list1[n].get("postCode"), list1[n].get("city"), list1[n].get("state"), list1[n].get("country"),
        #                       list1[n].get("phone"), list1[n].get("emailAddress"), list1[n].get("password"))
        rp.completeRegisterForm(fake.name(), fake.last_name(), formatted_date, fake.address(),
                                fake.postalcode(), fake.city(), fake.state(), fake.country(),
                               fake.random_number(10), fake.email(), list1[n].get("password"))
        assert lp.showLoginTitle() == "Login"
        # fake.date_of_birth().strftime("%d/%m/%Y")
        time.sleep(2)




