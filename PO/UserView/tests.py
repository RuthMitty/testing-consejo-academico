from PO.UserView.Tramites import Tramites
from PO.UserView import UserView

def test_create_request_to_consejo_academico(page):
    user_view = UserView(page)
    tramites = Tramites(page)
    user_view.select_tramites_tab()
    tramites.filter_in_search_bar()
    tramites.filter_in_search_bar()

