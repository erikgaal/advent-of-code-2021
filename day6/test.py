import unittest

from main import lanternsim

input = """3,4,3,1,2"""

class TestSonar(unittest.TestCase):
    def test_depth(self):
        self.assertEqual(26, lanternsim([int(x) for x in input.split(',')], max_days=18))

    def test_depth_aim(self):
        self.assertEqual(5934, lanternsim([int(x) for x in input.split(',')], max_days=80))

    def test_depth_aim(self):
        self.assertEqual(26984457539, lanternsim([int(x) for x in input.split(',')], max_days=256))

if __name__ == '__main__':
    unittest.main()
