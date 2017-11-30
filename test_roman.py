import unittest


def convert_to_roman(number):
    roman_dict = {
    1 : "I",
    5 : "V",
    10 : "X",
    50 : "L",
    100 : "C",
    500: "D",
    1000 : "M"
    }
    roman_number = ''
    exponential = 0 
    while(number != 0):
        last_digit = number%10
        roman_number = roman_dict.get(last_digit*(10**exponential)) + roman_number
        number=number//10
        exponential=exponential + 1
        
    return roman_number

class RomanNumeralsTest(unittest.TestCase):
    
    
    def test_defined_roman_number_1(self):
        self.assertEqual('I',convert_to_roman(1))
        
    def test_defined_roman_number_5(self):
        self.assertEqual("V",convert_to_roman(5))
        
    def test_undefined_roman_number_with_direct_multiples_of_defined_roman_numerals(self):
        self.assertEqual("XXV",convert_to_roman(25))
        
    def test_undefined_roman_number_without_multiples_of_defined_roman_numerals(self):
        self.assertEqual("III",conver_to_roman(3))