import argparse


def main():
    parser = argparse.ArgumentParser(description="Counter Strike CSStash Scraper")
    parser.add_argument("run", help="Command to run")
    args = parser.parse_args()

    if args.run == "run":
        print("Running cs-stash scraper")
        pass


if __name__ == "__main__":
    main()
