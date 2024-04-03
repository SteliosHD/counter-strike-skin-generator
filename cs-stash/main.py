import argparse
import time

from db.queries import Query
from db.session import get_initialized_session
from scraper import scrape


def main():
    parser = argparse.ArgumentParser(description="Counter Strike CSStash Scraper")
    parser.add_argument("run", help="Command to run")
    parser.add_argument("--weapon_urls", help="Scrape weapon urls", action="store_true")
    parser.add_argument("--skin_urls", help="Scrape skin urls", action="store_true")
    parser.add_argument("--skins", help="Scrape skins", action="store_true")
    args = parser.parse_args()
    if args.run == "run":
        print("Running cs-stash scraper")
        session, session_instance = get_initialized_session()
        query = Query(session)
        if args.weapon_urls:
            weapon_urls = scrape.run_weapons_scrape()
            for url in weapon_urls:
                if not query.get_url_by_url(url):
                    query.add_url(url)
        else:
            weapon_urls = query.get_all_urls_by_type(type_of_url="weapon")
        if args.skin_urls:
            skin_urls = []
            for index, weapon_url in enumerate(weapon_urls):
                print(f"Run skins scrape for weapon url {weapon_url} #{index+1}")
                scraped_skin_urls = scrape.run_skins_scrape(weapon_url)
                skin_urls.extend(scraped_skin_urls)
                for skin_url in scraped_skin_urls:
                    if not query.get_url_by_url(skin_url):
                        query.add_url(skin_url, type_of_url="skin")
                time.sleep(2)
        else:
            skin_urls = query.get_all_urls_by_type(type_of_url="skin")
        if args.skins:
            skins = []
            for index, skin_url in enumerate(skin_urls):
                print(f"Run skin scrape for skin url {skin_url} #{index+1}")
                skin = scrape.run_skin_scrape(skin_url)
                if not query.get_skin_by_url(skin["cs_stash_url"]):
                    query.add_skin(skin)
                skins.append(skin)
        else:
            skins = query.get_all_skins()
        print(skins[0])
        print(weapon_urls[0])
        print(skin_urls[0])


if __name__ == "__main__":
    main()
