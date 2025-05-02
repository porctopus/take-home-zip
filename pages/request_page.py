import re

class RequestPage:
    def __init__(
        self,
        page,
    ):

        self.page = page 
        
        # Buttons
        self.initial_price_edit_btn = page.get_by_role("button", name="Edit", exact=True).nth(1)
        self.save_btn = page.get_by_role("button", name="Save")
        self.updated_price_edit_btn = page.locator("span").filter(has_text="Updated price").get_by_label("Edit")

        # Headings
        self.request_heading = page.locator("div").filter(has_text=re.compile(r"^#83: Take home Challenge$"))

        # Nodes
        self.budget_approval_node = page.get_by_role("button", name="Add node Budget Approval").nth(1)
        self.department_approval_node = page.get_by_role("button", name="Add node Department Approval").nth(1)
        self.finalize_request_details = page.get_by_role("button", name="Add node Finalize request").nth(1)
        self.legal_approval_node = page.get_by_text("Ready to startLegal")
        self.manager_approval_node = page.get_by_text("Ready to startManager")

        # Sections
        self.agreement_details_section = page.locator("#rdp-contract-details-section")

        # Texboxes
        self.initial_price_textbox = page.get_by_role("textbox", name="Initial price")
        self.updated_price_textbox = page.get_by_role("textbox", name="Updated price")

        # Text
        self.initial_price_text = page.get_by_text("Initial price")
        self.updated_price_text = page.get_by_text("Updated price")

        # Toasts
        self.agreement_updated_toast = page.get_by_text("Agreement details successfully updated")

    def enter_price(self, price_type, new_price):
        """
        Set the initial or updated price.

        Args:
            price_type (str): "Initial" or "Updated"
            new_price (str): The value to set for the price
        """
        if price_type not in ["Initial", "Updated"]:
            raise ValueError("price_type must be 'Initial' or 'Updated'")

        # Dynamically get locators based on price_type
        price_text = self.page.get_by_text(f"{price_type} price")
        price_edit_btn = getattr(self, f"{price_type.lower()}_price_edit_btn")
        price_textbox = getattr(self, f"{price_type.lower()}_price_textbox")

        price_text.hover()
        price_edit_btn.click()
        price_textbox.clear()
        price_textbox.fill(new_price)
        self.save_btn.click()
        self.agreement_updated_toast.wait_for()
        self.agreement_updated_toast.wait_for(state="hidden")