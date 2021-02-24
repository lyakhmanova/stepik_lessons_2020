from selenium import webdriver

main_page_link = "http://selenium1py.pythonanywhere.com/ru"


def test_login_page_redirect():
    # Data
    expected_login_page_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(15)
        browser.get(main_page_link)

        # Act
        browser.find_element_by_id("login_link").click()

        # Assert

        login_page_link = browser.current_url
        assert expected_login_page_link in login_page_link, \
            "Incorrect url"


    finally:
        browser.quit()

test_login_page_redirect()
