from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class Home_Page(Page):
    RUSSIAN_LANGUAGE = (By.CSS_SELECTOR, "a#weglot-language-ru")
    ENGLISH_LANGUAGE = (By.CSS_SELECTOR, "a#weglot-language-en")

    def change_lang(self):
        self.click(*self.ENGLISH_LANGUAGE)
        self.click(*self.RUSSIAN_LANGUAGE)
        self.refresh()

    def verify_lang(self):
        self.verify_text(*self.RUSSIAN_LANGUAGE)
        assert "the Language is Russian"