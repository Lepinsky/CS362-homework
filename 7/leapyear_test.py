import unittest
from leapyear import leapyear


class TestLeapYear(unittest.TestCase):

    def test_leapyear(self):
        self.assertEqual(leapyear(2012), True)
        self.assertEqual(leapyear(400), True)
        self.assertEqual(leapyear(100), False)
        self.assertEqual(leapyear(231), False)

if __name__ == "__main__":
    unittest.main()
