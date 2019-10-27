import sqlite3
import requests

"""
Reports Table:
id integer | name text | frequency text | last_run text(date) | link text
"""


class DataCommunicator:
    """Instantiation will communicate with the local dB and MISO Energy API"""
    def __init__(self):
        self.db = 'energy_data.db'


    def test_conn(self):
        """Returns true if rows in the database are returned and conn is made to API, showing a good connection"""
        # flags for tests
        db_conn_good = False
        api_conn_good = False

        # test dB conn. Select query on reports > how many reports returned?
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

        # test API for response, so we can gather data
        r = requests.get('https://www.misoenergy.org/markets-and-operations/RTDataAPIs/')
        if r.status_code == requests.codes.ok:
            api_conn_good = True

        if db_conn_good and api_conn_good:
            return True
        else:
            return False

    def get_avail_reports_names(self):
        """Queries dB for names of reports, returns list of all reports"""
        reports_list = []

        conn = sqlite3.connect(self.db)
        curs = conn.cursor()
        curs.execute('SELECT name FROM Reports')
        for report_name in curs.fetchall():
            reports_list.append(report_name[0])

        conn.close()

        return reports_list
