


def test_progress(page):
    page.goto("http://uitestingplayground.com/")
    page.locator("text=Progress Bar").click()
    assert page.url == "http://uitestingplayground.com/progressbar"

    page.locator("button:has-text(\"Start\")").click()

    page.wait_for_selector("#progressBar[aria-valuenow='75']")

    page.locator("button:has-text(\"Stop\")").click()