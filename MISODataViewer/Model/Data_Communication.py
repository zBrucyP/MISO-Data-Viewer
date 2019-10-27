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
        # keep the id with the
        # {report_id: report_name, ...}
        reports_list = {}

        # connect to db and grab report ids and names
        conn = sqlite3.connect(self.db)
        curs = conn.cursor()
        curs.execute('SELECT id, name FROM Reports')

        # go through results to create dict
        for result in curs.fetchall():
            reports_list[result[0]] = (result[1])

        # close db connection
        conn.close()

        return reports_list

    def grab_report_data(self, report_id):
        """based on the report requested, makes a call to the API
            returns it in a dict
        """
        # connect to db, setup cursor
        conn = sqlite3.connect(self.db)
        curs = conn.cursor()

        # prepare query
        query = 'SELECT link FROM Reports WHERE id =' + report_id

        # run query
        curs.execute(query)

        # grab result from query
        url = curs.fetchone()[0]

        # get request to API
        r = requests.get(url)

        # test for good status
        if r.status_code == requests.codes.ok:
            # grab result. Converts json to dictionary
            res = r.json()

            return res
        else:
            return None


