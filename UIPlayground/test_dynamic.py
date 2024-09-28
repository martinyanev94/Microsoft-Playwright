

def test_dynamic(page):
    page.goto("http://uitestingplayground.com/")
    page.locator("a:has-text(\"Dynamic Table\")").click()
    assert page.url == "http://uitestingplayground.com/dynamictable"
    war_var = page.locator(".bg-warning").inner_text().split(" ")[2]

    table_list = page.locator("span[role=\"cell\"]").all_inner_texts()
    chrome_values = table_list[table_list.index("Chrome"):
                               table_list.index("Chrome")+5]
    tab_val = 'None'
    for value in chrome_values:
        if '%' in value:
            tab_val = value
            break

    print("Warning value: ", war_var)
    print("Table value: ", tab_val)
    assert tab_val == war_var

