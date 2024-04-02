def get_scraper_relative_path():
    return "cs-stash/"


def get_db_path():
    return f"sqlite:///{get_scraper_relative_path()}db/cs-stash.db"
