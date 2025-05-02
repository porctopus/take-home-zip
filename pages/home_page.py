class HomePage:
    def __init__(
        self,
        page,
    ):

        self.page = page 
        
        # Buttons
        self.settings_btn = page.get_by_role("button", name="Settings")
        self.log_out_btn = page.get_by_role("button", name="Log out")

        # Headings
        self.welcome_heading = page.get_by_role("heading", name="👋 Hi Zip, welcome back!")

    def logout(self):
        """
        Log out of the application
        """
        self.settings_btn.click()
        self.log_out_btn.click()