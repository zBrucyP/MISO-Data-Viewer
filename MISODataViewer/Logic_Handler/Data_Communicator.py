import sqlite3
import requests

"""
Reports Table:
id integer | name text | frequency text | last_run text(date) | link text
"""


class DataCommunicator:
    def __init__(self):
        self.db = 'energy_data.db'

    def test_conn(self):
        """Returns true if rows in the database are returned and conn is made to API, showing a good connection"""
        db_conn_good = False
        api_conn_good = False

        conn = sqlite3.connect(self.db)
        curs = conn.cursor()
        curs.execute('SELECT * FROM Reports')
        num_of_reports = len(curs.fetchall())
        print(str(num_of_reports) + ' reports found')
        conn.close()

        if num_of_reports > 1:
            db_conn_good = True
        else:
            return False

        r = requests.get('https://www.misoenergy.org/markets-and-operations/RTDataAPIs/')
        if r.status_code == requests.codes.ok:
            api_conn_good = True
        print(str(db_conn_good) + ' ' + str(api_conn_good))
        if db_conn_good and api_conn_good:
            return True
        else:
            return False

    def get_avail_reports(self):

