import unittest

from main import sonar

input = """199
200
208
210
200
207
240
269
260
263
"""

class TestSonar(unittest.TestCase):
    def test_sonar(self):
        self.assertEqual(7, sonar(input.splitlines()))

    def test_sonar_window(self):
        self.assertEqual(5, sonar(input.splitlines(), 3))

if __name__ == '__main__':
    unittest.main()
