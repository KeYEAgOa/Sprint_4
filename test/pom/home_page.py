import allure
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# Класс главной страницы
class HomePageScooter:
    yandex_logo = [By.XPATH, "//*[@class='Header_LogoYandex__3TSOI']"]

    # локатор на вопросы о важном
    questions_important = [By.XPATH, "//div[text()='Вопросы о важном']"]

    # локатор вниз
    locator_down = [By.XPATH, "//div[ text()='Когда аренда заканчивается']"]

    top_button_order = [By.XPATH, "//div[@class='Header_Nav__AGCXC']/button[text()='Заказать']"]

    def __init__(self, driver):
        self.driver = driver

    @allure.step('вызываем метод для скроллинга к разделу Вопросы о важном на странице Home page')
    def goto_questions_important(self):
        element = self.driver.find_element(*self.questions_important)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('вызываем метод для скроллинга к нижней кнопке Заказать на странице Home page')
    def goto_bottom_button(self):
        element = self.driver.find_element(*self.locator_down)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('вызываем метод кликнуть верхнюю кнопку Заказать на странице Home page')
    def click_top_button_order(self):
        self.driver.find_element(*self.top_button_order).click()

    @allure.step('вызываем метод кликнуть нижнюю кнопку Заказать на странице Home page')
    def click_bottom_button_order(self):
        self.goto_bottom_button()
        try:
            WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(
                (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']"))).click()
        except TimeoutException:
            return False

        return True

    @allure.step('вызываем метод проверить что мы находимся на странице Home page')
    def check_presence(self):
        try:
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
                (By.XPATH, "//*[@class='Home_Header__iJKdX' and contains(text(), 'Самокат ')]")))
        except TimeoutException:
            return False

        return True

    @allure.step('вызываем метод кликнуть лого Яндекс на странице Home page')
    def click_yandex_logo(self):
        self.driver.find_element(*self.yandex_logo).click()

        window_yandex = self.driver.window_handles[1]
        self.driver.switch_to.window(window_yandex)

        try:
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
                (By.XPATH, "//*[@aria-label='Яндекс']")))
        except TimeoutException:
            return False

        return True

    @allure.step(
        'вызываем метод получения и сравнения вопроса Сколько это стоит? И как оплатить? на странице Home page')
    def get_answer_for_price(self):

        try:
            WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(
                (By.XPATH, "//div[text() = 'Сколько это стоит? И как оплатить?']"))).click()

            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
                (By.XPATH, "//p[text() = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.']")))

        except TimeoutException:
            return False

        return True

    @allure.step(
        'вызываем метод получения и сравнения вопроса Хочу сразу несколько самокатов! Так можно? на странице Home page')
    def get_answer_for_amount_samokats(self):

        try:
            WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(
                (By.XPATH, "//div[text() = 'Хочу сразу несколько самокатов! Так можно?']"))).click()

            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
                (By.XPATH, "//p[text() = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.']")))

        except TimeoutException:
            return False

        return True

    @allure.step(
        'вызываем метод получения и сравнения вопроса Как рассчитывается время аренды? на странице Home page')
    def get_answer_for_time_of_rent(self):

        try:
            WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(
                (By.XPATH, "//div[text() = 'Как рассчитывается время аренды?']"))).click()

            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
                (By.XPATH, "//p[text() = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.']")))

        except TimeoutException:
            return False

        return True

    @allure.step(
        'вызываем метод получения и сравнения вопроса Можно ли заказать самокат прямо на сегодня? на странице Home page')
    def get_answer_for_posible_to_order_today(self):

        try:
            WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(
                (By.XPATH, "//div[text() = 'Можно ли заказать самокат прямо на сегодня?']"))).click()

            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
                (By.XPATH, "//p[text() = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.']")))

        except TimeoutException:
            return False

        return True

    @allure.step(
        'вызываем метод получения и сравнения вопроса Можно ли продлить заказ или вернуть самокат раньше? на странице Home page')
    def get_answer_for_posible_to_return_early(self):

        try:
            WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(
                (By.XPATH, "//div[text() = 'Можно ли продлить заказ или вернуть самокат раньше?']"))).click()

            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
                (By.XPATH, "//p[text() = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.']")))

        except TimeoutException:
            return False

        return True

    @allure.step(
        'вызываем метод получения и сравнения вопроса Вы привозите зарядку вместе с самокатом? на странице Home page')
    def get_answer_for_delivery_battarey(self):

        try:
            WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(
                (By.XPATH, "//div[text() = 'Вы привозите зарядку вместе с самокатом?']"))).click()

            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
                (By.XPATH, "//p[text() = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.']")))

        except TimeoutException:
            return False

        return True

    @allure.step(
        'вызываем метод получения и сравнения вопроса Можно ли отменить заказ? на странице Home page')
    def get_answer_for_cansel_order(self):

        try:
            WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(
                (By.XPATH, "//div[text() = 'Можно ли отменить заказ?']"))).click()

            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
                (By.XPATH, "//p[text() = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.']")))

        except TimeoutException:
            return False

        return True

    @allure.step(
        'вызываем метод получения и сравнения вопроса Я живу за МКАДом, привезёте? на странице Home page')
    def get_answer_for_order_from_mkad(self):

        try:
            WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(
                (By.XPATH, "//div[text() = 'Я жизу за МКАДом, привезёте?']"))).click()

            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
                (By.XPATH, "//p[text() = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.']")))

        except TimeoutException:
            return False

        return True

