from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.request_page import RequestPage

def test_price_change_update(env, page, data):
    login_page = LoginPage(env, page)
    request_page = RequestPage(page)

    user = data["user"]
    password = data["password"]
    request_url = env["request_url"]
    initial_price = "80.00"
    updated_price = "230.00"
    price_change = f"{float(updated_price) - float(initial_price):.2f}"

    # Login and navigate to approval request page
    login_page.login(user, password)
    page.goto(request_url)
    
    # Set the initial price
    request_page.enter_price("Initial", initial_price)

    # Confirm the initial price is updated
    expect(request_page.agreement_details_section).to_contain_text(f"Initial priceUSD ${initial_price}")

    # Set the updated price
    request_page.enter_price("Updated", updated_price)

    # Confirm the updated price is updated
    expect(request_page.agreement_details_section).to_contain_text(f"Updated priceUSD ${updated_price}")

    # Confirm the price change is updated correctly
    expect(request_page.agreement_details_section).to_contain_text(f"Price changeUSD ${price_change}")