from selenium.webdriver.common.by import By
from pages.base_page import Page
from support.logger import logger
from time import sleep


class Mobile_Menu_Page(Page):
    ENGLISH_MENU = (By.CSS_SELECTOR, '.wg-dd-1-togle-3')
    RUSSIAN_MENU = (By.CSS_SELECTOR, 'a.wg-dropdown-1-link-2')
    MOBILE_MENU = (By.CSS_SELECTOR, "div.mobile-top-menu")

    def change_lang(self):
        self.click(*self.MOBILE_MENU)
        self.click(*self.ENGLISH_MENU)
        self.click(*self.RUSSIAN_MENU)
        sleep(5)
        self.refresh()