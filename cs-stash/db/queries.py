from db.schema import ScrapedUrl, Skin


class Query:
    def __init__(self, session):
        self.session = session

    def get_all_skins(self):
        return self.session.query(Skin).all()

    def get_all_urls(self):
        return self.session.query(ScrapedUrl).all()
