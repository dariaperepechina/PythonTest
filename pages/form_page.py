import time

from selenium.webdriver import Keys

from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocators as Locators


class FormPage(BasePage):

    def fill_fields_and_submit(self):
        first_name = 'Ivan'
        last_name = 'Ivanov'
        email = 'ivan@mail.com'

        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(Locators.LAST_NAME).send_keys(last_name)
        self.element_is_visible(Locators.EMAIL).send_keys(email)
        self.element_is_visible(Locators.GENDER).click()
        self.element_is_visible(Locators.MOBILE).send_keys('6546897897')
        subject = self.element_is_visible(Locators.SUBJECT)
        subject.send_keys('English')
        subject.send_keys(Keys.RETURN)
        self.element_is_visible(Locators.HOBBIES).click()
        self.element_is_visible(Locators.FILE_INPUT).send_keys(
            r'C:\Users\Пользователь\PycharmProjects\PythonTest\test.txt')
        self.element_is_visible(Locators.CURRENT_ADDRESS).send_keys('Moscow, Lenina 12')
        self.element_is_visible(Locators.SUBMIT).click()
        self.element_is_visible(Locators.STATE).click()
        self.element_is_visible(Locators.STATE_LIST).click()
        self.element_is_visible(Locators.CITY).click()
        self.element_is_visible(Locators.CITY_LIST).click()
        return first_name, last_name, email

    def form_result(self):
        result_list = self.elements_are_visible(Locators.RESULT_TABLE)
        result_text = []

        for i in result_list:
            result_text.append(i.text)

        return result_text

    def open(self):
        pass
