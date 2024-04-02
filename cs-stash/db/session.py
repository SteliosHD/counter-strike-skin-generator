from sqlalchemy.orm import sessionmaker

from . import schema


class Session:
    def __init__(self, engine):
        self.engine = engine
        self.session = None

    def init_session(self):
        try:
            session = sessionmaker(bind=self.engine)
            self.session = session()
            print("Session created successfully")
        except Exception as e:
            print(f"Error: {e}")
            return None

    def get_session(self):
        return self.session

    def close_session(self):
        self.session.close()
        print("Session closed successfully")


def get_initialized_session():
    session_instance = Session(schema.get_engine())
    session_instance.init_session()
    return session_instance.get_session(), session_instance


if __name__ == "__main__":
    Session(schema.get_engine())
    print("Session created successfully")
