from playwright.sync_api import Page, expect


def test_example_title(page: Page):
    page.goto("https://example.com")
    expect(page).to_have_title("Example Domain")


def test_example_has_heading(page: Page):
    page.goto("https://example.com")
    heading = page.get_by_role("heading", name="Example Domain")
    expect(heading).to_be_visible()