
def test_frame(page):
    page.goto(
        "https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe")
    # Click pre[role="presentation"]:has-text("​")
    page.frame_locator(
        "text=Try it Each embedded browsing context has its own session history and document.  >> iframe").locator(
        "pre[role=\"presentation\"]:has-text(\"​\")").click()
    # Fill #html-editor textarea
    page.frame_locator(
        "text=Try it Each embedded browsing context has its own session history and document.  >> iframe").locator(
        "#html-editor textarea").fill("My favorite tool is playwright")
