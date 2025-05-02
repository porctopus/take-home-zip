from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.request_page import RequestPage

def test_approval_condition(env, page, data):
    login_page = LoginPage(env, page)
    request_page = RequestPage(page)

    user = data["user"]
    password = data["password"]
    request_url = env["request_url"]
    low_price = "50"
    mid_price = "250"
    high_price = "501"

    # Login and navigate to approval request page
    login_page.login(user, password)
    page.goto(request_url)
    
    # Set the updated price below the first threshold
    request_page.enter_price("Updated", low_price)

    # Confirm the workflow is updated
    expect(request_page.legal_approval_node).to_be_visible()
    expect(request_page.department_approval_node).to_be_visible()
    expect(request_page.finalize_request_details).to_be_visible()
    expect(request_page.budget_approval_node).not_to_be_visible()
    expect(request_page.manager_approval_node).not_to_be_visible()

    # Set the updated price between the first and second threshold
    request_page.enter_price("Updated", mid_price)

    # Confirm the workflow is updated
    expect(request_page.legal_approval_node).to_be_visible()
    expect(request_page.department_approval_node).to_be_visible()
    expect(request_page.finalize_request_details).to_be_visible()
    expect(request_page.budget_approval_node).to_be_visible()
    expect(request_page.manager_approval_node).not_to_be_visible()

    # Set the updated price above the second threshold
    request_page.enter_price("Updated", high_price)

    # Confirm the workflow is updated
    expect(request_page.legal_approval_node).to_be_visible()
    expect(request_page.department_approval_node).to_be_visible()
    expect(request_page.finalize_request_details).to_be_visible()
    expect(request_page.budget_approval_node).to_be_visible()
    expect(request_page.manager_approval_node).to_be_visible()