import allure
from selene import browser, be, by
from selene.support.shared.jquery_style import s


def test_with_lambda():
    with allure.step("Открываем главую страницу GitHub"):
        browser.open("/")

    with allure.step("Ищем репозиторий"):
        s(by.text('Search or jump to...')).click()
        s('#query-builder-test').send_keys("CptVasilver/python_homework8")
        s('#query-builder-test').submit()

    with allure.step("Проверяем наличие #1 Issue"):
        s(by.link_text("CptVasilver/python_homework8")).click()
        s("#issues-tab").click()
        s(by.partial_text("#1")).should(be.visible)
