import unittest
from stringCal import add

class TestStringCal(unittest.TestCase):

    def test_emptyStringReturnsZero(self):
        self.assertEqual(add(""), 0)
    def test_singleNumberReturnsSameNumber(self):
        self.assertEqual(add("4"), 4)
    def test_twoNumbersReturnsSum(self):
        self.assertEqual(add("1,2"), 3)
    def test_multipleNumbersReturnsSum(self):
        self.assertEqual(add("1,2,3,4"), 10)
    def test_newlineAsDelimiter(self):
        self.assertEqual(add("1\n2,3"), 6)
    def test_customDelimiter(self):
        self.assertEqual(add("//;\n1;2"), 3)
     
if __name__ == '__main__':
    unittest.main()
