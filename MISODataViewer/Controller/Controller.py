import datetime
import sys, os
from MISODataViewer.Model import Data_Communication
from datetime import timedelta


class Controller:
    def __init__(self):
        self.last_good_api_db_test = None
        self.model = Data_Communication.DataCommunicator()

    def is_connection_good(self):
        """checks when last test was. If >15 minutes, retest. Otherwise, assume true
            cuts down on API calls
        """
        if self.last_good_api_db_test == None:
            if self.model.test_conn() == True:
                #self.set_last_good_api_db_test()
                return True
            else:
                return False
        else:
            # get the difference in time between now and when connection was last tested
            # if > 15 minutes, test again
            # otherwise, assume it is good
            now = datetime.datetime.now()
            duration = now - self.last_good_api_db_test
            duration_in_s = duration.total_seconds()
            minutes = divmod(duration_in_s, 60)[0]

            if minutes > 15:
                if self.model.test_conn() == True:
                    self.set_last_good_api_db_test()
                    return True
                else:
                    return False
            else:
                return True


    """ TODO: Fix, store last test of api/db 
    def set_last_good_api_db_test(self):
        # sets the last test time as now, updates file
        now = datetime.datetime.now()
        self.last_good_api_db_test = now
        with open(os.path.join(sys.path[0], 'last_api_db_test'), 'w') as outfile:
            outfile.write(now)


    def get_last_good_api_db_test(self):
        # gets the last api/db test time from file
        datetime_line = ''
        with open(os.path.join(sys.path[0], 'last_api_db_test'), 'r') as infile:
            datetime_line = infile.readline()

        self.last_good_api_db_test = datetime.fromisoformat(datetime_line)
    """


    def get_avail_reports_names(self):
        return self.model.get_avail_reports_names()