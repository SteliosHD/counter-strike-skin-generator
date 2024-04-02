from db.schema import ScrapedUrl, Skin


class Query:
    def __init__(self, session):
        self.session = session

    def get_all_skins(self):
        return self.session.query(Skin).all()

    def get_all_urls(self):
        return self.session.query(ScrapedUrl).all()

    def get_url_by_url(self, url):
        return self.session.query(ScrapedUrl).filter(ScrapedUrl.url == url).first()

    def get_all_urls_by_type(self, type_of_url):
        return [
            entry.url for entry in self.session.query(ScrapedUrl).filter(ScrapedUrl.type_of_url == type_of_url).all()
        ]

    def add_url(self, url, type_of_url="weapon"):
        new_url = ScrapedUrl(url=url, scraped_status=False, type_of_url=type_of_url)
        self.session.add(new_url)
        self.session.commit()
        return new_url
