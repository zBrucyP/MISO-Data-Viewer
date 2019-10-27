import unittest
from MISODataViewer.Model import Data_Communication

# print results from grab_report_data(self, report_id)
# should always return either None or json data as a dict from the API
dc = Data_Communication.DataCommunicator()
res = dc.grab_report_data(1)
print(res)

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
