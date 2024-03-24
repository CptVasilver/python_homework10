import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_with_decorator():
    open_main_page()
    search_repo("CptVasilver/python_homework8")
    go_to_repo("CptVasilver/python_homework8")
    issue_check("#1")


@allure.step("Открываем главую страницу GitHub")
def open_main_page():
    browser.open("/")


@allure.step("Ищем репозиторий {repo}")
def search_repo(repo):
    s(by.text('Search or jump to...')).click()
    s('#query-builder-test').send_keys(repo)
    s('#query-builder-test').submit()


@allure.step("Переходим в репозиторий {repo}")
def go_to_repo(repo):
    s(by.link_text(repo)).click()


@allure.step("Проверяем наличие {issue} Issue")
def issue_check(issue):
    s("#issues-tab").click()
    s(by.partial_text(issue)).should(be.visible)
