import allure
from playwright.sync_api import Page, expect


@allure.epic("SauceDemo")
@allure.feature("Авторизация")
@allure.story("Успешный вход")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Логин с валидными данными")
def test_login_success(page: Page):
    with allure.step("Открыть страницу логина"):
        page.goto("https://www.saucedemo.com/")

    with allure.step("Ввести username"):
        page.get_by_placeholder("Username").fill("standard_user")

    with allure.step("Ввести password"):
        page.get_by_placeholder("Password").fill("secret_sauce")

    with allure.step("Нажать Login"):
        page.get_by_role("button", name="Login").click()

    with allure.step("Проверить, что мы на странице товаров"):
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")