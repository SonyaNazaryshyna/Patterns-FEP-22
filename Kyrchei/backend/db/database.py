from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from backend.config import MARIADB_HOST, MARIADB_USERNAME, MARIADB_PASSWORD, MARIADB_DATABASE, MARIADB_PORT

class DBConnection:
    __instance = None

    def __init__(self):
        self.sessio = None
        self.session: sessionmaker
        self.engine = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls, *args, **kwargs)
            cls.__instance.__connection = None
        return cls.__instance

    def connect(self):
        self.engine = create_engine(
            f'mysql+mysqlconnector://{MARIADB_USERNAME}:{MARIADB_PASSWORD}@{MARIADB_HOST}:{MARIADB_PORT}/{MARIADB_DATABASE}',
            connect_args={
                'collation': "utf8mb4_unicode_ci",
                'charset': 'utf8mb4'
            }
        )
        Session = sessionmaker(bind=self.engine)
        self.sessio = Session()

    def test(self, query: str):
        self.sessio.execute(text(query))

    def disconnect(self):
        self.sessio.close()


