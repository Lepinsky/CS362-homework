import unittest
from volume import volume
from average import average
from fullname import fullname


class TestCalculator(unittest.TestCase):

    #Volume
    def test_volume(self):
        #Valid Inputs
        #Rounds to the 6th decimal point
        self.assertEqual(volume(2), 8)
        self.assertEqual(volume(12.21), 1820.316861)

        #Code can run string format version of float value
        self.assertEqual(volume("1.2"), 1.728)

        #Invalid inputs
        #Code returns -1 on invalid input

        #String
        self.assertEqual(volume("a"), -1)
        self.assertEqual(volume("]'\'"), -1)
        self.assertEqual(volume(""), -1)
        self.assertEqual(volume("12.21.3"), -1)

        #Negative
        self.assertEqual(volume(-12), -1)

        #Zero (treated as invalid)
        self.assertEqual(volume(0), -1)

    #Average
    def test_average(self):
        #Valid Inputs
        #Rounds to the 6th decimal point
        self.assertEqual(average([1, 2, 3]), 2) #Positive
        self.assertEqual(average([-1, -2, -3, -10]), -4) #Negative
        self.assertEqual(average([-1, -12, -1]), -4.666667) #Fraction Average
        self.assertEqual(average([1.2]), 1.2) #Fraction in list

        #Invalid Inputs
        #Returns False on error
        self.assertFalse(average([])) #Empty list
        self.assertFalse(average([1, 2, "a"])) #Invalid type in list
        self.assertFalse(average(["a"])) #Invalid type


    #Full Name
    def test_name(self):
        #Valid Inputs
        self.assertEqual(fullname("John", "Smith"), "John Smith")
        self.assertEqual(fullname("Jane", "Doe"), "Jane Doe")

        #Invalid Inputs
        #Returns False on error
        self.assertFalse(fullname("", "")) #Empty Name
        self.assertFalse(fullname("12", "213")) #Number name
        self.assertFalse(fullname("][]", "[]")) #Invalid Characters

if __name__ == "__main__":
    unittest.main()
