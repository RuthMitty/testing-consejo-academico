import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # headless=False para ver el navegador
        yield browser
        browser.close()


@pytest.fixture
def context(browser):
    context = browser.new_context()

    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )

    yield context

    # ruta al trace
    context.tracing.stop(path="trace.zip")
    context.close()


@pytest.fixture
def page(context):
    page = context.new_page()
    page.goto("http://localhost:5173/")
    yield page
    page.close()