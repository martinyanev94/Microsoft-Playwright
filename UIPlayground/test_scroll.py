from playwright.sync_api import expect


def test_scroll(page):
    page.goto("http://uitestingplayground.com/")
    page.locator("text=Scrollbars").click()
    assert page.url == "http://uitestingplayground.com/scrollbars"
    page.locator("text=ScrollbarsAn application may use native or custom "
                 "scrollbars and some elements m >> div").nth(2).click()
    page.mouse.wheel(100, 100)
    expect(page.locator(".btn-primary")).to_have_text(
        "Hiding Button")
    page.locator(".btn-primary").click()
