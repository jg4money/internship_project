from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class Login_Page(Page):
    EMAIL_FIELD = (By.CSS_SELECTOR, "#email-2")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input#field")
    LOGIN_BTTN = (By.CSS_SELECTOR, "a.login-button")

    def open_main(self):
        self.driver.get('https://soft.reelly.io/sign-in/')
        self.driver.refresh()

    def login(self):
        self.wait_for_element_clickable(*self.EMAIL_FIELD)
        self.input_text(*self.EMAIL_FIELD,'grabledjacob@gmail.com')
        self.input_text(*self.PASSWORD_FIELD, 'Coolio14')
        self.click(*self.LOGIN_BTTN)
