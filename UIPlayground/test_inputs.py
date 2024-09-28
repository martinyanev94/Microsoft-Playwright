from playwright.sync_api import expect


def test_form(page):
    page.goto("http://uitestingplayground.com/")
    page.locator("text=Text Input").click()
    assert page.url == "http://uitestingplayground.com/textinput"
    page.locator(".form-control").click()
    page.locator(".form-control").fill("New button name")
    page.locator(".btn-primary").click()
    expect(page.locator(".btn-primary")).to_have_text("New button name")
    page.locator(".form-control").fill("Newer name")
    page.locator(".form-control").press("Enter")
    expect(page.locator(".btn-primary")).not_to_have_text("Newer name")
    page.locator(".form-control").fill("Hi")
    page.locator(".btn-primary").click()
    expect(page.locator(".btn-primary")).to_have_text("Hi")


