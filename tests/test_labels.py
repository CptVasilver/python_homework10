import allure
from allure_commons.types import Severity
from selene.support.shared.jquery_style import s
from selene import browser, be, by


@allure.title("Просмотр issue в репозитории")
@allure.description("Открытие репозитория, поиск #1 issue")
@allure.suite("tests")
@allure.id("1004")
@allure.sub_suite("test_allure_labels")
@allure.issue("issue")
@allure.testcase("testcase")
@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "CptVasilver")
@allure.feature("Issue в репозитории")
@allure.story("Просмотр Issue в репозитории")
@allure.link("https://github.com", name="Testing")
def test_issue_on_github_with_annotations():
    browser.open("/")

    s(by.text('Search or jump to...')).click()
    s('#query-builder-test').send_keys("CptVasilver/python_homework8")
    s('#query-builder-test').submit()

    s(by.link_text("CptVasilver/python_homework8")).click()
    s("#issues-tab").click()
    s(by.partial_text("#1")).should(be.visible)
