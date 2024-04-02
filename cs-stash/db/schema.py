from sqlalchemy import (
    Boolean,
    Column,
    Float,
    ForeignKey,
    Integer,
    LargeBinary,
    String,
    create_engine,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy_utils import ChoiceType
from utils.utils import get_db_path

RARITY_CHOICES = (
    ("Consumer Grade", "Consumer Grade"),
    ("Industrial Grade", "Industrial Grade"),
    ("Mil-Spec", "Mil-Spec"),
    ("Restricted", "Restricted"),
    ("Classified", "Classified"),
    ("Covert", "Covert"),
    ("Contraband", "Contraband"),
)


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
    scraped_status = Column(Boolean)
    parent_id = Column(Integer, ForeignKey("scraped_urls.id"))
    child_url = relationship(
        "ScrapedUrl",
        primaryjoin="ScrapedUrl.id==ScrapedUrl.parent_id",
        remote_side=[id],
    )

    def __repr__(self):
        return f"<ScrapedURL(key={self.url})>"


class Skin(Base):
    __tablename__ = "skins"

    id = Column(Integer, primary_key=True)
    skin_name = Column(String)
    rarity = ChoiceType(RARITY_CHOICES)
    weapon_type = Column(String)
    stat_trak = Column(Boolean)
    factory_new_price = Column(Float)
    texture_image = Column(LargeBinary)
    cs_stash_url = Column(String)

    def __repr__(self):
        return f"<Skin(name={self.name}, price={self.price})>"


if __name__ == "__main__":
    get_engine()
    print("Database created successfully")
