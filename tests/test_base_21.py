from playwright.sync_api import Page, expect


def test_click_link(page: Page):
    page.goto("https://example.com")
    page.locator("a").click()
    expect(page).to_have_url("https://www.iana.org/help/example-domains")