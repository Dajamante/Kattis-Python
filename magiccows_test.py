from best_relay import BestRelay
import unittest


class TestBestRelay(unittest.TestCase):

    def test_make_start_times_dic(self):
        br = BestRelay()
        runners = """ 6
                    ASHMEADE 9.90 8.85
                    BLAKE 9.69 8.72
                    BOLT 9.58 8.43
                    CARTER 9.78 8.93
                    FRATER 9.88 8.92
                    POWELL 9.72 8.61 """

        start_times = br.make_start_times_dic(runners)

        right_answer = {"ASHMEADE" : 9.90,
                        "BLAKE" : 9.69,
                        "BOLT" : 9.58,
                        "CARTER": 9.78,
                        "FRATER": 9.88,
                        "POWELL": 9.72 }
        self.assertEqual(right_answer, start_times)


    def test_make_warm_times_dic(self):
        br = BestRelay()
        runners = """ 6
                    ASHMEADE 9.90 8.85
                    BLAKE 9.69 8.72
                    BOLT 9.58 8.43
                    CARTER 9.78 8.93
                    FRATER 9.88 8.92
                    POWELL 9.72 8.61 """

        warm_times = br.make_warm_times_dic(runners)

        right_answer = {"ASHMEADE" : 8.85,
                        "BLAKE" : 8.72,
                        "BOLT" : 8.43,
                        "CARTER": 8.93,
                        "FRATER": 8.92,
                        "POWELL": 8.61 }
        self.assertEqual(right_answer, warm_times)