# def test_instagram(page):
#     page.goto("https://www.instagram.com")
#     page.locator("text=Forgot password?").click()
#     page.wait_for_url("https://www.instagram.com/accounts/password/reset/")
#     page.screenshot(path="sc1.png")
#     page.locator("text=Create New Account").click()
#     page.wait_for_url("https://www.instagram.com/accounts/emailsignup/")
#
#     page.locator("[aria-label=\"Mobile Number or Email\"]").click()
#     page.screenshot(path="sc2.png")
#     page.locator("[aria-label=\"Mobile Number or Email\"]").fill(
#         "playwright@gmail.com")
#     page.locator("[aria-label=\"Full Name\"]").click()
#     page.locator("[aria-label=\"Full Name\"]").fill("Play")
#     page.locator("[aria-label=\"Full Name\"]").press("Tab")
#     page.locator("[aria-label=\"Username\"]").fill("wright3536462")
#     page.locator("[aria-label=\"Password\"]").click()
#     page.locator("[aria-label=\"Password\"]").fill("wright1234")
#     page.screenshot(path="sc3.png")
#     page.locator("button:has-text(\"Sign up\")").click()


def test_facebook(browser):
    # browser --> context --> page

    context = browser.new_context()
    context.tracing.start(snapshots=True, sources=True)
    page = context.new_page()
    page.goto("https://www.facebook.com/register")
    page.locator("[aria-label=\"First name\"]").click()
    page.locator("[aria-label=\"First name\"]").fill("Jack")
    page.locator("[aria-label=\"First name\"]").press("Tab")

    page.locator("[aria-label=\"Last name\"]").fill("Jones")
    page.locator("[aria-label=\"Mobile number or email\"]").click()
    page.locator("[aria-label=\"Mobile number or email\"]").fill("123456")
    page.locator("[aria-label=\"Mobile number or email\"]").press("Tab")

    page.locator("[aria-label=\"New password\"]").fill("12345678")

    page.locator("[aria-label=\"Month\"]").select_option("9")
    page.locator("[aria-label=\"Day\"]").select_option("23")
    page.locator("[aria-label=\"Year\"]").select_option("2011")

    page.locator("input[name=\"sex\"]").nth(1).check()
    page.locator("button[name=\"websubmit\"]").click()
    context.tracing.stop(path="tracing.zip")
