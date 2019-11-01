import unittest
from Main.run_test import RunTest


class TestGetSearchPrompt(unittest.TestCase):

    def setUp(self):
        self.run = RunTest(1)

    def test_001(self):
        expect, authentic = self.run.go_on_run(1)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_002(self):
        expect, authentic = self.run.go_on_run(2)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

