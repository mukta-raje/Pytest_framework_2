import pytest

from faker import Faker
from pageObjects.login_page import Login_Page_Class
from pageObjects.Registraion_page import Registration_Page_Class
from utilities.ReadConfig import ReadConfigClass

@pytest.mark.usefixtures("driver_setup")
class Test_User_Profile_Class:
    driver = None
    email = ReadConfigClass.get_data_for_email()
    password = ReadConfigClass.get_data_for_password()
    login_url = ReadConfigClass.get_data_for_login_url()
    register_url = ReadConfigClass.get_data_for_register_url()


    def test_CardKart_Title_001(self):
        self.driver.get(self.login_url)
        self.driver.maximize_window()


        if self. driver.title == "CredKart":
            print("you are landed on correct page and it's title is:", self.driver.title)
            assert True
        else:
            print("you are landed on wrong page and it's title is:", self.driver.title)
            assert False


    def test_CredKart_Login_002 (self):

        self.driver.get(self.login_url)
        self.lp = Login_Page_Class(self.driver)

        self.lp.Enter_Email(self.email)
        self.lp.Enter_Password(self.password)
        self.lp.Click_Submit_Button()


        if self.lp.verify_menu() == "pass":
            self.lp.Click_menu_button()
            self.lp.click_logout_link()


        else:
            self.driver.save_screenshot(r"D:\Automation Testing\Pytest_framework_2\Screenshots\User login Failed.png")




    def test_CredKart_Registration_003(self):
        self.driver.get(self.register_url)
        self.rp = Registration_Page_Class(self.driver) # Object Creation
        name = Faker().name()
        email = Faker().email()
        print(f"Name: {name}, Email: {email}")
        # Field - Name
        self.rp.Enter_Name(name)

        # Field - Email
        self.rp.Enter_Email(email)

        # Field - Password
        self.rp.Enter_Password("Credence@123")

        # Field - Confirm Password
        self.rp.Enter_Confirm_Password("Credence@123")

        # Button - Submit
        self.rp.Click_Submit_Button() # registration button

        if self.rp.verify_menu() == "Pass":

             self.rp.Click_menu_button()
             self.rp.click_logout_link()


        else:
            self.driver.save_screenshot(r"D:\Automation Testing\Pytest_framework_2\Screenshots\User Registration Failed1.png")


