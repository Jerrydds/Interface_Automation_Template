import unittest
from main.run_test import RunTest


class TestGetSearchPrompt(unittest.TestCase):

    def setUp(self):
        self.run = RunTest(1)

    def test_001(self):
        self.run.go_on_run(1)

    def test_002(self):
        self.run.go_on_run(2)



