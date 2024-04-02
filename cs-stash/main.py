import argparse

from db.queries import Query
from db.session import get_initialized_session
from scraper import scrape


def main():
    parser = argparse.ArgumentParser(description="Counter Strike CSStash Scraper")
    parser.add_argument("run", help="Command to run")
    parser.add_argument("--weapon_urls", help="Scrape weapon urls", action="store_true")
    args = parser.parse_args()
    if args.run == "run":
        print("Running cs-stash scraper")
        session, session_instance = get_initialized_session()
        query = Query(session)
        print(query.get_all_skins())
        weapon_urls = scrape.run("weapon_urls") if args.weapon_urls else query.get_all_weapon_urls()
        for url in weapon_urls:
            if not query.get_url_by_url(url):
                query.add_url(url)
        print(weapon_urls)


if __name__ == "__main__":
    main()
