import allure
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# Класс страницы заказа
class OrderPageScooter:
    samokat_logo = [By.XPATH, "//*[@class='Header_LogoScooter__3lsAR']"]

    input_name = [By.XPATH, "//input[@placeholder='* Имя']"]

    input_surname = [By.XPATH, "//input[@placeholder='* Фамилия']"]

    input_address = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]

    input_metro = [By.XPATH, "//input[@placeholder='* Станция метро']"]

    input_phone = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]

    button_next = [By.XPATH, "//button[text()='Далее']"]

    input_day = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]

    menu_time = [By.XPATH, "//div[@class='Dropdown-placeholder' and text()='* Срок аренды']"]

    color_black = [By.XPATH, "//input[@id='black']"]

    color_grey = [By.XPATH, "//input[@id='grey']"]

    input_comment = [By.XPATH, "//input[@placeholder='Комментарий для курьера']"]

    button_order = [By.XPATH, "//button[text()='Заказать' and @class='Button_Button__ra12g Button_Middle__1CSJM']"]

    def __init__(self, driver):
        self.driver = driver

    @allure.step('вызываем метод Создаем заказ на странице Заказов')
    def place_order(self, name, surname, address, metro, phone, day, time, color, comment):

        try:
            # проверить что открыта форма "Для кого самокат"
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
                (By.XPATH, "//div[text()='Для кого самокат']")))

            self.driver.find_element(*self.input_name).send_keys(name)
            self.driver.find_element(*self.input_surname).send_keys(surname)
            self.driver.find_element(*self.input_address).send_keys(address)

            self.driver.find_element(*self.input_metro).click()
            metro_xpath = "//*[text()='" + metro + "']"
            WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(
                (By.XPATH, metro_xpath))).click()

            self.driver.find_element(*self.input_phone).send_keys(phone)
            self.driver.find_element(*self.button_next).click()

            # проверить что открыта форма "Про аренду"
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
                (By.XPATH, "//div[text()='Про аренду']")))

            self.driver.find_element(*self.input_day).click()
            day_xpath = "//div[@class='react-datepicker__day react-datepicker__day--" + day + " react-datepicker__day--weekend']"
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
                (By.XPATH, day_xpath))).click()

            self.driver.find_element(*self.menu_time).click()
            time_xpath = "//*[text()='" + time + "']"
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
                (By.XPATH, time_xpath))).click()

            if color == 'black':
                self.driver.find_element(*self.color_black).click()
            elif color == 'grey':
                self.driver.find_element(*self.color_grey).click()
            elif color == 'both':
                self.driver.find_element(*self.color_black).click()
                self.driver.find_element(*self.color_grey).click()

            self.driver.find_element(*self.input_comment).send_keys(comment)
            self.driver.find_element(*self.button_order).click()

            # нажать кнопку хотите оформить заказ Да
            WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(
                (By.XPATH, "//button[text()='Да']"))).click()

            # проверить что заказ оформлен
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
                (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")))

        except TimeoutException:
            return False

        return True

    @allure.step('вызываем метод кликнуть лого Самокат на странице Заказов')
    def click_samokat_logo(self):
        self.driver.find_element(*self.samokat_logo).click()

    
