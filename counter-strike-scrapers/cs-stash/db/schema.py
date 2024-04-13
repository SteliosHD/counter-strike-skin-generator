from sqlalchemy import Boolean, Column, Integer, LargeBinary, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import ChoiceType
from utils.utils import get_db_path

Base = declarative_base()


def get_engine(sqlite_db_path=get_db_path()):
    try:
        engine = create_engine(sqlite_db_path)
        Base.metadata.create_all(engine)
        print("Database created successfully on db/cs-stash.db")
    except Exception as e:
        print(f"Error: {e}")
        return None
    return engine


class ScrapedUrl(Base):
    __tablename__ = "scraped_urls"

    id = Column(Integer, primary_key=True)
    url = Column(String)
    type_of_url = Column(ChoiceType([("weapon", "weapon"), ("skin", "skin"), ("other", "other")], impl=String()))
    scraped_status = Column(Boolean)

    def __repr__(self):
        return f"<ScrapedURL(key={self.url})>"


class Skin(Base):
    __tablename__ = "skins"

    id = Column(Integer, primary_key=True)
    skin_name = Column(String)
    quality = Column(String)
    weapon_name = Column(String)
    stat_trak = Column(Boolean)
    factory_new_price = Column(String)
    texture_image = Column(LargeBinary, nullable=True)
    cs_stash_url = Column(String)
    texture_url = Column(String, nullable=True)

    def __repr__(self):
        return f"<Skin(name={self.skin_name}, price={self.factory_new_price})>"


if __name__ == "__main__":
    get_engine()
    print("Database created successfully")
