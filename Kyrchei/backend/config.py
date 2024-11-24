import os
from dotenv import load_dotenv

load_dotenv()

NBA_API_KEY = os.getenv("NBA_API_KEY")
MARIADB_USERNAME = os.getenv("MARIADB_ROOT_USERNAME")
MARIADB_PASSWORD = os.getenv("MARIADB_ROOT_PASSWORD")
MARIADB_DATABASE = os.getenv("MARIADB_DATABASE")
MARIADB_PORT = os.getenv("MARIADB_PORT")
MARIADB_HOST = os.getenv("MARIADB_HOST")
HEADERS = {"Authorization": f"{NBA_API_KEY}"}