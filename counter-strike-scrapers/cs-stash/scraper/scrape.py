import asyncio

import requests
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


async def scrape_skins(url):
    async with async_playwright() as pw:
        browser = await pw.chromium.launch()
        page = await browser.new_page()
        await page.goto(url)
        await page.click('text="Agree and proceed"')
        weapon_title = await page.query_selector("h2")
        weapon_title_text = await weapon_title.text_content()
        title_content = weapon_title_text.split("|")
        weapon_name = title_content[0].strip()
        skin_name = title_content[1].strip()
        stat_trak = True if await page.locator(".stattrak").count() else False
        quality = await page.locator(".quality").inner_text()
        price_selector = 'span:text("Factory new") + span'
        price_text_selectors = page.locator(price_selector)
        price_text = (
            await price_text_selectors.nth(0).text_content() if await price_text_selectors.count() > 0 else "-1"
        )
        img_locator = page.locator('img[alt="Skin Pattern File"]')
        image_source = await img_locator.get_attribute("src") if await img_locator.count() > 0 else None
        image = download_image_as_blob(image_source) if image_source else None
        return {
            "weapon_name": weapon_name,
            "skin_name": skin_name,
            "stat_trak": stat_trak,
            "quality": quality,
            "factory_new_price": price_text,
            "cs_stash_url": url,
            "texture_image": image,
            "texture_url": image_source,
        }


def run_weapons_scrape():
    return asyncio.run(scrape_href_links(CS_STASH_URL))


def run_skins_scrape(url):
    return asyncio.run(scrape_skins_href_links(url))


def run_skin_scrape(url):
    return asyncio.run(scrape_skins(url))


def download_image_as_blob(image_url):
    response = requests.get(image_url)
    response.raise_for_status()
    return response.content


if __name__ == "__main__":
    asyncio.run(scrape_href_links(CS_STASH_URL))
