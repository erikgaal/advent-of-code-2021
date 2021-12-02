import unittest

from main import depth

input = """forward 5
down 5
forward 8
up 3
down 8
forward 2
"""

class TestSonar(unittest.TestCase):
    def test_depth(self):
        self.assertEqual(150, depth(input.splitlines()))

    def test_depth_aim(self):
        self.assertEqual(900, depth(input.splitlines(), True))

if __name__ == '__main__':
    unittest.main()
