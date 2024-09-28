

# def test_microsoft(page):
#     page.goto("https://microsoft.com")
#     page.locator("text=Shop Surface deals").click()
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page()
    page.goto("http://playwright.dev")
    print(page.title())
    page.pause()
    page.goto("https://cnn.com")
    browser.close()