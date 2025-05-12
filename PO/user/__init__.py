from playwright.sync_api import Page

class UserView:
    def __init__(self, page: Page):
        self.page = page

    def select_home_tab(self):
        self.page.get_by_role("link", name="Realizar Solicitud").click()

    def select_tramites_tab(self):
        self.page.get_by_role("link", name="Trámites").click()

    def select_rastrear_tab(self):
        self.page.get_by_role("link", name="Rastrear").click()