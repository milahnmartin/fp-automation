import sqlite3


class Db:
    def __init__(self) -> None:

        self.conn = sqlite3.connect('../logs.db')
        self.cur = self.conn.cursor()

    def create_table(self) -> None:
        self.cur.execute("CREATE TABLE `fp_logs`()")

    def query(self, query):
