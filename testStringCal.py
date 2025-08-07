import unittest
from stringCal import add

class TestStringCal(unittest.TestCase):

    def test_emptyStringReturnsZero(self):
        self.assertEqual(add(""), 0)
    def test_singleNumberReturnsSameNumber(self):
        self.assertEqual(add("4"), 4)#single number
    def test_twoNumbersReturnsSum(self):
        self.assertEqual(add("1,2"), 3)#two numbers 
    def test_multipleNumbersReturnsSum(self):
        self.assertEqual(add("1,2,3,4"), 10)#multiple numbers
     
if __name__ == '__main__':
    unittest.main()
