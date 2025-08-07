import unittest
from stringCal import add

class TestStringCal(unittest.TestCase):

    def test_emptyStringReturnsZero(self):
        self.assertEqual(add(""), 0)
    def test_singleNumberReturnsSameNumber(self):
        self.assertEqual(add("4"), 4)
    def test_twoNumbersReturnsSum(self):
        self.assertEqual(add("1,2"), 3)
     
if __name__ == '__main__':
    unittest.main()
