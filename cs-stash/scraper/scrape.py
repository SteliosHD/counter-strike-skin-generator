import asyncio

from playwright.async_api import async_playwright

CS_STASH_URL = "https://csgostash.com/"


async def scrape_href_links(url):
    async with async_playwright() as pw:
        browser = await pw.chromium.launch()
        page = await browser.new_page()
        await page.goto(url)
        await page.click('text="Agree and proceed"')
        # The pattern you're looking for in the href attribute.
        href_pattern = "/weapon/"

        # Find all <ul> elements. You might need to adjust this selector based on the page structure.
        ul_elements = await page.query_selector_all("ul")

        # Initialize a list to hold all matching hrefs.
        matching_hrefs = []

        for ul in ul_elements:
            # For each <ul>, find all child <a> tags and filter based on the href attribute containing the pattern.
            # This uses a JavaScript function executed in the page context to filter the <a> elements.
            hrefs = await ul.eval_on_selector_all(
                "a",
                f"""
                elements => elements
                    .map(element => element.href)
                    .filter(href => href.includes("{href_pattern}"))
            """,
            )
            matching_hrefs.extend(hrefs)
        await browser.close()
        print("Weapon URLs run was successfully")
        return matching_hrefs


def run(option):
    if option == "weapon_urls":
        return asyncio.run(scrape_href_links(CS_STASH_URL))


if __name__ == "__main__":
    asyncio.run(scrape_href_links(CS_STASH_URL))
