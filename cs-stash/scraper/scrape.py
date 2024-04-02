import asyncio

from playwright.async_api import async_playwright

CS_STASH_URL = "https://csgostash.com/"
URLS = {CS_STASH_URL: {"search_button_queries": ["Pistols", "Rifles", "Knives", "Mid-Tier"]}}


async def main(url):
    metadata = URLS.get(url)
    if not metadata:
        print("Invalid URL")
        return
    async with async_playwright() as pw:
        browser = await pw.chromium.launch()
        page = await browser.new_page()
        await page.goto(url)
        await page.click('text="Agree and proceed"')
        await page.screenshot(path="cs-stash/screenshots/main.png")
        #
        # for query in metadata["search_button_queries"]:
        #     await page.click(f'text="{query}"')
        #     await page.wait_for_timeout(5000)
        #     await page.screenshot(path=f"cs-stash/screenshots/{query}.png")
        await browser.close()
        print("Screenshots saved successfully")


def run():
    asyncio.run(main(CS_STASH_URL))


if __name__ == "__main__":
    asyncio.run(main(CS_STASH_URL))
