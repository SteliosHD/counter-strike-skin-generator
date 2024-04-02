import argparse

from db.queries import Query
from db.session import get_initialized_session


def main():
    parser = argparse.ArgumentParser(description="Counter Strike CSStash Scraper")
    parser.add_argument("run", help="Command to run")
    args = parser.parse_args()

    if args.run == "run":
        print("Running cs-stash scraper")
        session, session_instance = get_initialized_session()
        query = Query(session)
        print(query.get_all_skins())
        pass


if __name__ == "__main__":
    main()
