from selene.support.shared.jquery_style import s
from selene import browser, be, by

def test_with_selene():
    browser.open("/")

    s(by.text('Search or jump to...')).click()
    s('#query-builder-test').send_keys("CptVasilver/python_homework8")
    s('#query-builder-test').submit()

    s(by.link_text("CptVasilver/python_homework8")).click()
    s("#issues-tab").click()
    s(by.partial_text("#1")).should(be.visible)
