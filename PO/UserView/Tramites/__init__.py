from playwright.sync_api import Page
from playwright.sync_api import expect

class Tramites:
    def __init__(self, page: Page):
        self.page = page

    def filter_in_search_bar(self):
        self.page.get_by_role("textbox", name="Buscar...").click()
        self.page.get_by_role("textbox", name="Buscar...").fill("solicitud de examen voluntario")
        self.page.get_by_text("Solicitud de examen voluntario").nth(1).click()

    def create_request(self):
        self.page.get_by_role("link", name="Realizar Solicitud").click()
        expect(self.page.get_by_role("heading", name="Solicitud de examen voluntario")).to_be_visible()

