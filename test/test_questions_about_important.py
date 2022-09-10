import allure
from selenium import webdriver

from pom.home_page import HomePageScooter


class TestQuestionsAboutImportant:

    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера Firefox
        cls.driver = webdriver.Firefox()

    def setup(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")

    @allure.title('Проверка ответа на вопрос: Сколько это стоит? И как оплатить?')
    @allure.description(
        'ответ должен содержать строку: Сутки — 400 рублей. Оплата курьеру — наличными или картой.')
    @allure.testcase('ссылка на тест-кейс', 'TestCase-001')
    def test_answer_for_price(self):
        hps = HomePageScooter(self.driver)
        hps.goto_questions_important()
        assert hps.get_answer_for_price()

    @allure.title('Проверка ответа на вопрос: Хочу сразу несколько самокатов! Так можно?')
    @allure.description(
        'ответ должен содержать строку: Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.')
    @allure.testcase('ссылка на тест-кейс', 'TestCase-002')
    def test_amount_samokats(self):
        hps = HomePageScooter(self.driver)
        hps.goto_questions_important()
        assert hps.get_answer_for_amount_samokats()

    @allure.title('Проверка ответа на вопрос: Как рассчитывается время аренды?')
    @allure.description(
        'ответ должен содержать строку: Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.')
    @allure.testcase('ссылка на тест-кейс', 'TestCase-003')
    def test_time_of_rent(self):
        hps = HomePageScooter(self.driver)
        hps.goto_questions_important()
        assert hps.get_answer_for_time_of_rent()

    @allure.title('Проверка ответа на вопрос: Можно ли заказать самокат прямо на сегодня?')
    @allure.description(
        'ответ должен содержать строку: Только начиная с завтрашнего дня. Но скоро станем расторопнее.')
    @allure.testcase('ссылка на тест-кейс', 'TestCase-004')
    def test_posible_to_order_today(self):
        hps = HomePageScooter(self.driver)
        hps.goto_questions_important()
        assert hps.get_answer_for_posible_to_order_today()

    @allure.title('Проверка ответа на вопрос: Можно ли продлить заказ или вернуть самокат раньше?')
    @allure.description(
        'ответ должен содержать строку: Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.')
    @allure.testcase('ссылка на тест-кейс', 'TestCase-005')
    def test_posible_to_return_early(self):
        hps = HomePageScooter(self.driver)
        hps.goto_questions_important()
        assert hps.get_answer_for_posible_to_return_early()

    @allure.title('Проверка ответа на вопрос: Вы привозите зарядку вместе с самокатом?')
    @allure.description(
        'ответ должен содержать строку: Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.')
    @allure.testcase('ссылка на тест-кейс', 'TestCase-006')
    def test_delivery_battarey(self):
        hps = HomePageScooter(self.driver)
        hps.goto_questions_important()
        assert hps.get_answer_for_delivery_battarey()

    @allure.title('Проверка ответа на вопрос: Можно ли отменить заказ?')
    @allure.description(
        'ответ должен содержать строку: Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.')
    @allure.testcase('ссылка на тест-кейс', 'TestCase-007')
    def test_cansel_order(self):
        hps = HomePageScooter(self.driver)
        hps.goto_questions_important()
        assert hps.get_answer_for_cansel_order()

    @allure.title('Проверка ответа на вопрос: Я живу за МКАДом, привезёте?')
    @allure.description('ответ должен содержать строку: Да, обязательно. Всем самокатов! И Москве, и Московской области.')
    @allure.testcase('ссылка на тест-кейс', 'TestCase-008')
    def test_order_from_mkad(self):
        hps = HomePageScooter(self.driver)
        hps.goto_questions_important()
        assert hps.get_answer_for_order_from_mkad()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
