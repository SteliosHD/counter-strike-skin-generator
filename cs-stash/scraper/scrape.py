import asyncio

from playwright.async_api import async_playwright

CS_STASH_URL = "https://csgostash.com/"


async def scrape_href_links(url):
    async with async_playwright() as pw:
        browser = await pw.chromium.launch()
        page = await browser.new_page()
        await page.goto(url)
        await page.click('text="Agree and proceed"')
        href_pattern = "/weapon/"
        ul_elements = await page.query_selector_all("ul")
        matching_hrefs = []
        for ul in ul_elements:
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


async def scrape_skins_href_links(url):
    async with async_playwright() as pw:
        browser = await pw.chromium.launch()
        page = await browser.new_page()
        await page.goto(url)
        await page.click('text="Agree and proceed"')
        href_pattern = "/skin/"
        js_filter_function = f"""
            Array.from(document.querySelectorAll('a'))
                .filter(a => a.href.includes("{href_pattern}"))
                .map(a => a.href)
        """
        matching_hrefs = await page.evaluate(js_filter_function)
        await browser.close()
        print("Skin URLs run was successfully")
        return list(set(matching_hrefs))


def run_weapons_scrape():
    return asyncio.run(scrape_href_links(CS_STASH_URL))


def run_skins_scrape(url):
    return asyncio.run(scrape_skins_href_links(url))


if __name__ == "__main__":
    asyncio.run(scrape_href_links(CS_STASH_URL))
