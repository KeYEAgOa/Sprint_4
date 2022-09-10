import pytest
import allure
from selenium import webdriver
from pom.home_page import HomePageScooter
from pom.order_page import OrderPageScooter


@pytest.fixture(scope="class")
def order1():
    return {"name": "свинка", "surname": "розовая", "address": "Москва Свинарный проезд 10",
            "metro": "Черкизовская", "phone": "84955550001", "day": "010", "time": "двое суток",
            "color": "black", "comment": "no comment"}


@pytest.fixture(scope="class")
def order2():
    return {"name": "лошадка", "surname": "пегая", "address": "Москва Лошадиная улица 20",
            "metro": "Сокольники", "phone": "84955550002", "day": "011", "time": "трое суток",
            "color": "grey", "comment": "no comment"}


@pytest.mark.usefixtures("order1", "order2")
class TestOrderSamokat:

    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера Firefox
        cls.driver = webdriver.Firefox()

    def setup(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")

    @allure.title('Проверка заказа через верхнюю кнопку с первым набором параметров для заказа')
    @allure.description('Проверить, что появилось всплывающее окно с сообщением об успешном создании заказа.')
    @allure.testcase('ссылка на тест-кейс', 'TestCase-009')
    def test_order_by_top_button_with_order1_set(self, order1):
        hps = HomePageScooter(self.driver)
        hps.click_top_button_order()

        ops = OrderPageScooter(self.driver)
        assert ops.place_order(order1['name'], order1['surname'], order1['address'], order1['metro'], order1['phone'],
                        order1['day'], order1['time'], order1['color'], order1['comment'])

    @allure.title('Проверка заказа через нижнюю кнопку со вторым набором параметров для заказа')
    @allure.description('Проверить, что появилось всплывающее окно с сообщением об успешном создании заказа.')
    @allure.testcase('ссылка на тест-кейс', 'TestCase-010')
    def test_order_by_bottom_button_with_order2_set(self, order2):
        hps = HomePageScooter(self.driver)
        hps.click_bottom_button_order()

        ops = OrderPageScooter(self.driver)
        assert ops.place_order(order2['name'], order2['surname'], order2['address'], order2['metro'], order2['phone'],
                        order2['day'], order2['time'], order2['color'], order2['comment'])

    @classmethod
    def teardown_class(cls):
        # Закрой браузер
        cls.driver.quit()
