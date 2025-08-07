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
    def test_newlineAsDelimiter(self):
        self.assertEqual(add("1\n2,3"), 6) #newline as delimiter
    def test_customDelimiter(self):
        self.assertEqual(add("//;\n1;2"), 3) #custom delimiter
    def test_negativeNumbersThrowException(self):
        with self.assertRaises(Exception) as context:
            add("1,-2,3,-4")
        self.assertIn("negative numbers not allowed -2,-4", str(context.exception))#neg number will throw exception
    def test_whitespaceOnlyReturnsZero(self):
        self.assertEqual(add("   "), 0) #handle whitespace
    def test_multiLengthDelimiter(self):
        self.assertEqual(add("//[***]\n1***2***3"), 6) # support delimiters of any length 
    def test_extractDelimiters_multiLength(self):
        self.assertEqual(add("//[***][%]\n1***2%3"), 6)
    def test_numbersGreaterThan1000AreIgnored(self):
        self.assertEqual(add("2,1001,3"), 5) #already source file handle this verify numbers greater than 1000 are ignored

     
if __name__ == '__main__':
    unittest.main()
