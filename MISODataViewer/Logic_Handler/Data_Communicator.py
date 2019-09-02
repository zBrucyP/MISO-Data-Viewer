import sqlite3

class data_communicator:
    def __init__(self):
        self.conn = sqlite3.connect('energy_data.db')
        self.curs = self.conn.cursor()

        self.curs.execute('SELECT * FROM Reports')
        print(self.curs.fetchall())