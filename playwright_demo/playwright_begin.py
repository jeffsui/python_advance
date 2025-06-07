from playwright.sync_api import Playwright,sync_playwright

def run(playwright:Playwright):
    brower= playwright.chromium.launch(headless=False)
    context = brower.new_context()
    page = context.new_page()
    page.goto("https://bing.com")
    page.wait_for_timeout(2000)
    context.close()
    brower.close()

with sync_playwright() as playwright:
    run(playwright)