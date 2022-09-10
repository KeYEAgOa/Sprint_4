import allure
from selenium import webdriver
from pom.home_page import HomePageScooter
from pom.order_page import OrderPageScooter


class TestOrderSamokat:

    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера Firefox
        cls.driver = webdriver.Firefox()

    def setup(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")

    @allure.title('Проверить: если нажать на логотип Самоката, попадёшь на главную страницу Самоката')
    @allure.description('Для проверки сначала переходим на страницу Заказа и нажимаем логотип Самоката')
    @allure.testcase('ссылка на тест-кейс', 'TestCase-011')
    def test_click_samokat_logo(self):
        hps = HomePageScooter(self.driver)
        hps.click_top_button_order()

        ops = OrderPageScooter(self.driver)
        ops.click_samokat_logo()

        assert hps.check_presence()

    @allure.title('Проверить: если нажать на логотип Яндекса, в новом окне откроется главная страница Яндекса.')
    @allure.description('Для проверки после нажатия на логотип Яндекса переходим в новое окно и проверя, что там загружен главная страница Яндекса')
    @allure.testcase('ссылка на тест-кейс', 'TestCase-012')
    def test_click_yandex_logo(self):
        hps = HomePageScooter(self.driver)
        assert hps.click_yandex_logo()

    @classmethod
    def teardown_class(cls):
        # Закрой браузер
        cls.driver.quit()
