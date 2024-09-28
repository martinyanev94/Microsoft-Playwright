from playwright.sync_api import expect


def test_click(page):
    page.goto("http://uitestingplayground.com/")
    page.locator("a:has-text(\"Mouse Over\")").click()
    assert page.url == "http://uitestingplayground.com/mouseover"

    page.locator("text=Click me").click()
    page.locator("text=Click me").click()
    # page.locator("text=Click me").doubleclick()

    expect(page.locator(".badge-light")).to_have_text("2")

