

def test_cover(page):
    page.goto("http://uitestingplayground.com/")
    page.locator("text=Overlapped Element").click()
    assert page.url == "http://uitestingplayground.com/overlapped"

    page.locator("[placeholder=\"Id\"]").click()
    page.locator("[placeholder=\"Id\"]").fill("1")

    page.mouse.wheel(0, 15)

    page.locator("[id=\"name\"]").click()
    page.locator("[id=\"name\"]").fill("Champ")