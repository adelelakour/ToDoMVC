from playwright.sync_api import Playwright, Page, Expect, expect
from urllib3.util import wait
import re


def test_clear_completed_todos(page:Page):
    page.goto("https://todomvc.com/examples/react/dist/")
    page.get_by_placeholder("What needs to be done?").fill("Renew my passport")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_placeholder("What needs to be done?").fill("Renew my driving license")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_placeholder("What needs to be done?").fill("Do one Playwright project")
    page.get_by_placeholder("What needs to be done?").press("Enter")

    renew_passport = page.locator("li").filter(has_text="Renew my passport")
    renew_passport.locator('input[type="checkbox"]').check()
    page.get_by_role("button", name="Clear completed").click()
    page.get_by_role("link", name="Completed").click()
    expect(page.locator("body")).not_to_contain_text("Renew my passport")
