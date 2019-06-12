import psycopg2
from dotenv import load_dotenv
load_dotenv()

connection_string = os.environ.get("TEST_DB_CREATION_CONN", "dbname=postgres")
conn = psycopg2.connect(connection_string)
conn.autocommit = True # Must be set to create databases

cur = conn.cursor()
cur.execute("create database actions_test")
