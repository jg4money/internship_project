from pages.base_page import Page
from pages.login_page import Login_Page
from pages.home_page import Home_Page


class Application:
    def __init__(self, driver):
        self.base_page = Page(driver)
        self.home_page = Home_Page(driver)
        self.login_page = Login_Page(driver)