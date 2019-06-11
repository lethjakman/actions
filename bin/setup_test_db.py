import psycopg2

conn = psycopg2.connect(dbname='postgres')
conn.autocommit = True # Must be set to create databases

cur = conn.cursor()
cur.execute("create database actions_test")
