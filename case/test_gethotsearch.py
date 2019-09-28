import unittest
from main.run_test import RunTest


class TestGetHotSearch(unittest.TestCase):

    def setUp(self):
        self.run = RunTest(0)

    def test_001(self):
        self.run.go_on_run(1)
        # print("case执行完成")

    def test_002(self):
        self.run.go_on_run(2)
