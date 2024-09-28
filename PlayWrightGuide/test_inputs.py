# def test_facebook(page):
#
#     page.goto("https://www.facebook.com/register")
#     page.locator("[aria-label=\"First name\"]").click()
#     page.locator("[aria-label=\"First name\"]").fill("Jack")
#     page.locator("[aria-label=\"First name\"]").press("Tab")
#
#     page.locator("[aria-label=\"Last name\"]").fill("Jones")
#     page.locator("[aria-label=\"Mobile number or email\"]").click()
#     page.locator("[aria-label=\"Mobile number or email\"]").fill("123456")
#     page.locator("[aria-label=\"Mobile number or email\"]").press("Tab")
#
#     page.locator("[aria-label=\"New password\"]").fill("12345678")
#
#     page.locator("[aria-label=\"Month\"]").select_option("9")
#     page.locator("[aria-label=\"Day\"]").select_option("23")
#     page.locator("[aria-label=\"Year\"]").select_option("2011")
#
#     page.locator("input[name=\"sex\"]").nth(1).check()
#     page.locator("button[name=\"websubmit\"]").click()


# def test_checkbox(page):
#     page.goto("https://www.w3.org/WAI/ARIA/apg/example-index/checkbox/checkbox")
#     page.locator("li:has-text(\"Sprouts\")").click()
#
#     sprouts = page.locator("div[role=\"checkbox\"]:has-text(\"Sprouts\")")
#     sprouts.click()
#
#     assert sprouts.is_checked() is True
#
#     mustard = page.locator("div[role=\"checkbox\"]:has-text(\"Mustard\")")
#     mustard.click()
#
#     assert mustard.is_checked() is True
#
#     page.locator("div[role=\"checkbox\"]:has-text(\"Lettuce\")").click()
#
#     page.locator("div[role=\"checkbox\"]:has-text(\"Tomato\")").click()


# def test_type(page):
#     page.goto("https://www.google.com/")
#     page.locator("[aria-label=\"Search\"]").click()
#     page.locator("[aria-label=\"Search\"]").type("social media")
#     page.locator("[aria-label=\"Search\"]").press("Enter")

def test_upload(page):
    page.goto("https://www.filemail.com/share/upload-file")
    page.locator("text=Add Files").click()

    page.locator("#addBtn input[type=\"file\"]").set_input_files(
        "/Users/martinyanev/Desktop/PlayWrightGuide/test1.txt")

    page.locator("button:has-text(\"Send\")").click()






