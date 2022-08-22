from selene.support.shared import browser
from selene import be, have

# Positive test
def test_able_to_find_text(open_google):
    query = browser.element('[name="q"]')
    query.should(be.blank).type('selene').press_enter()
    browser.element('#search').should(have.text('User-oriented Web UI browser tests in Python'))

# Negative test
def test_unable_to_find_text(open_google):
    query = browser.element('[name="q"]')
    query.should(be.blank).type('abcdefg').press_enter()
    browser.element('#search').should(have.text('User-oriented Web UI browser tests in Python'))