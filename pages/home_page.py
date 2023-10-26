from selenium.webdriver.common.by import By
from pages.base_page import Page
from support.logger import logger
from time import sleep


class Home_Page(Page):
    RUSSIAN_LANGUAGE = (By.CSS_SELECTOR, "a#weglot-language-ru")
    ENGLISH_LANGUAGE = (By.CSS_SELECTOR, "a#weglot-language-en")
    VERIFY_RUSSIAN = (By.XPATH, '//html[@lang="ru"]')
    MOBILE_MENU = (By.CSS_SELECTOR, "div.mobile-top-menu")

    def change_lang(self):
        self.click(*self.MOBILE_MENU)
        self.click(*self.ENGLISH_LANGUAGE)
        self.click(*self.RUSSIAN_LANGUAGE)
        sleep(5)
        self.refresh()

    def verify_lang(self):
        self.find_element(*self.VERIFY_RUSSIAN)

    assert "the Language is Russian"
