from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class Login_Page(Page):
    EMAIL_FIELD = (By.ID, 'email-2')
    PASSWORD_FIELD = (By.ID, "field")
    LOGIN_BTTN = (By.CSS_SELECTOR, "a.login-button")

    def open_main(self):
        self.driver.get('https://soft.reelly.io/sign-in/ ')
        self.driver.refresh()
        #sleep(5)- add to run in firefox


    def login(self):
        self.input_text('grabledjacob@gmail.com', *self.EMAIL_FIELD)
        self.input_text('Coolio14', *self.PASSWORD_FIELD)
        self.click(*self.LOGIN_BTTN)
