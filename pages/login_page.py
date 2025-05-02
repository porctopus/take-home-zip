class LoginPage:
    def __init__(
        self,
        env,
        page,
    ):
        self.page = page
        self.url = env["url"] + "/login"

        # Buttons
        self.login_btn = page.get_by_test_id("loginButton")

        # Headings
        self.sign_in_to_zip_heading = page.get_by_role("heading", name="Sign in to Zip")

        # Links
        self.sign_in_to_google_link = page.get_by_role("link", name="Sign in with Google")
        self.forgot_password_link = page.locator("[data-test=\"z-link\"]")
        
        # Textboxes
        self.email_textbox = page.get_by_role("textbox", name="Email")
        self.password_textbox = page.get_by_role("textbox", name="Password")

    def click_next_button(self):
        """
        Click the Next button on the login page
        """
        with self.page.expect_response(
            lambda response: ("graphql" in response.url)
            and response.status == 200
            and response.request.method == "POST"
        ):
            self.login_btn.click()

    def click_login_button(self):
        """
        Click the Login button
        """
        with self.page.expect_response(
            lambda response: ("login" in response.url)
            and response.status == 200
            and response.request.method == "POST"
        ):
            self.login_btn.click()

    def go_to_login_page(self):
        """
        Navigates to the login page
        """
        self.page.goto(self.url)

    def login(self, username, password):
        """
        Login with the specified user

        Args:
            username (str): user name to log in with
            password (str): user's password
        """
        self.go_to_login_page()
        self.email_textbox.fill(username)
        self.click_next_button()
        self.password_textbox.fill(password)
        self.click_login_button()