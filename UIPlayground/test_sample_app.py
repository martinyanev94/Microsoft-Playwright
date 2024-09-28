from playwright.sync_api import expect


def test_login(page):
    page.goto("http://uitestingplayground.com/")
    page.locator("text=Sample App").click()
    assert page.url == "http://uitestingplayground.com/sampleapp"

    page.locator("[placeholder=\"User\\ Name\"]").click()
    page.locator("[placeholder=\"User\\ Name\"]").fill("Martin")

    page.locator("[placeholder=\"User\\ Name\"]").press("Tab")

    page.locator("[placeholder=\"\\*\\*\\*\\*\\*\\*\\*\\*\"]").click()
    page.locator("[placeholder=\"\\*\\*\\*\\*\\*\\*\\*\\*\"]").fill("pwd")

    page.locator("text=Log In").click()
    expect(page.locator(".text-success")).to_have_text("Welcome, Martin!")
    page.locator("text=Log Out").click()
    expect(page.locator(".text-info")).to_have_text("User logged out.")