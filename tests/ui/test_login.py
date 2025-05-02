from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.home_page import HomePage

def test_login(env, page, data):
    login_page = LoginPage(env, page)
    home_page = HomePage(page)

    user = data["user"]
    password = data["password"]

    # Navigate to login page and confirm modal elements
    login_page.go_to_login_page()
    expect(login_page.sign_in_to_zip_heading).to_be_visible(timeout=2000)
    expect(login_page.sign_in_to_google_link).to_be_visible()
    expect(login_page.email_textbox).to_be_visible()
    expect(login_page.login_btn).to_be_visible()

    # Enter email and click Next
    login_page.email_textbox.fill(user)
    login_page.click_next_button()

    # Confirm Password and Forgot Password link are displayed
    expect(login_page.password_textbox).to_be_visible(timeout=2000)
    expect(login_page.forgot_password_link).to_be_visible()

    # Enter password and log in
    login_page.password_textbox.fill(password)
    login_page.click_login_button()

    # Confirm elements on the home page after login
    expect(home_page.welcome_heading).to_be_visible(timeout=5000)

    # Log out
    home_page.logout()    
