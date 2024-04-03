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

    def get_skin_by_url(self, url):
        return self.session.query(Skin).filter(Skin.cs_stash_url == url).first()

    def add_skin(self, skin):
        skin_data = {
            "skin_name": skin["skin_name"],
            "quality": skin["quality"],
            "weapon_name": skin["weapon_name"],
            "stat_trak": skin["stat_trak"],
            "factory_new_price": skin["factory_new_price"],
            "cs_stash_url": skin["cs_stash_url"],
        }
        if skin["texture_image"]:
            skin_data["texture_image"] = skin["texture_image"]
        if skin["texture_url"]:
            skin_data["texture_url"] = skin["texture_url"]
        new_skin = Skin(**skin_data)
        self.session.add(new_skin)
        self.session.commit()
        return new_skin

    def add_url(self, url, type_of_url="weapon"):
        new_url = ScrapedUrl(url=url, scraped_status=False, type_of_url=type_of_url)
        self.session.add(new_url)
        self.session.commit()
        return new_url
