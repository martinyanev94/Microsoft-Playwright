from playwright.sync_api import expect


# def test_load_display(page):
#     page.goto('http://uitestingplayground.com/')
#     page.locator("text=Load Delay").click()
#     assert page.url == "http://uitestingplayground.com/loaddelay"
#     page.locator("text=Button Appearing After Delay").click()


# def test_ajax(page):
#     page.goto('http://uitestingplayground.com/')
#     page.locator("text=AJAX Data").click()
#     assert page.url == "http://uitestingplayground.com/ajax"
#     page.locator(".btn-primary").click()
#     expect(page.locator(".bg-success")).to_have_text("Data loaded with AJAX "
#                                                      "get request.",
#                                                      timeout=16000)

def test_button_change(page):
    page.goto('http://uitestingplayground.com/')
    page.locator("a:has-text(\"Click\")").click()
    assert page.url == "http://uitestingplayground.com/click"
    expect(page.locator(".btn-primary")).to_have_text("Button That Ignores"
                                                      " DOM Click Event")
    page.locator(".btn-primary").click()
    expect(page.locator(".btn-success")).to_have_text("Button That Ignores"
                                                      " DOM Click Event")







