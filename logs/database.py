import sqlite3
from datetime import datetime


class Db:
    def __init__(self) -> None:

        self.conn = sqlite3.connect('../logs.db')
        self.cur = self.conn.cursor()

    def create_table(self) -> None:
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS fp_logs (id integer PRIMARY KEY AUTOINCREMENT,date TEXT,game TEXT,query TEXT,last_response INETEGER);")
        print("[FP-LOGS DATABASE CREATION ACTION INITIATED]")

    def query(self, game: str, query: str, last_response: int):
        now = datetime.now()
        self.conn.execute("INSERT INTO `fp_logs(`date`,`game`,`query`,`last_response`)VALUES({},{},{},{});".format(
            now, game, query, last_response))
        self.conn.commit()
        print("[FP-LOGS QUERY INSTERTED INTO DB]")
