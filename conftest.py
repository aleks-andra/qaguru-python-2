import pytest
from selene.support.shared import browser

# Starting Google
@pytest.fixture()
def open_google():
    browser.open('https://www.google.com/')

# Setting up window size
def window_size():
    browser.config.window_width = 1400
    browser.config.window_height = 900
