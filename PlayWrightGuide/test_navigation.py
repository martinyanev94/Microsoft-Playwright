def test_navigator(page):
    page.goto("https://www.instagram.com")
    page.locator("text=Forgot password?").click()
    page.wait_for_url("https://www.instagram.com/accounts/password/reset/")

    page.locator("text=Create New Account").click()
    page.wait_for_url("https://www.instagram.com/accounts/emailsignup/")

    page.locator("[aria-label=\"Mobile Number or Email\"]").click()
    page.locator("[aria-label=\"Mobile Number or Email\"]").fill(
        "playwright@gmail.com")
    page.locator("[aria-label=\"Full Name\"]").click()
    page.locator("[aria-label=\"Full Name\"]").fill("Play")
    page.locator("[aria-label=\"Full Name\"]").press("Tab")
    page.locator("[aria-label=\"Username\"]").fill("wright3536462")
    page.locator("[aria-label=\"Password\"]").click()
    page.locator("[aria-label=\"Password\"]").fill("wright1234")
    page.locator("button:has-text(\"Sign up\")").click()