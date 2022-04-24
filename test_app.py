import unittest
from app import Calculations
from app import Helper
from app import Parser

class MyTestCase(unittest.TestCase):

    #unit tests
    def test_add(self):
        self.assertEqual(Calculations.add(2,3), 5)

    def test_sub(self):
        self.assertEqual(Calculations.sub(4,3), 1)

    def test_mult(self):
        self.assertEqual(Calculations.mult(4,3), 12)

    def test_div(self):
        self.assertEqual(Calculations.div(4,4), 1)
    
    def test_find_all_operations(self):
        eq = "2*8*2+4/4-3"
        self.assertEqual(Helper.find_all_operations(eq), [1,3,5,7,9])

    def test_recurisvemult_multanddiv(self):
        eq = "2*8*4/4"
        self.assertEqual(Parser.recursivemult(eq), '16')

    def test_recurisvemult_only_mult(self):
        eq = "12*12"
        self.assertEqual(Parser.recursivemult(eq), '144')

    def test_recurisvemult_mult_with_addition_before(self):
        eq = "2+2+12*12"
        self.assertEqual(Parser.recursivemult(eq), '2+2+144')

    def test_recurisvemult_mult_with_addition_after(self):
        eq = "2+2+12*12+2"
        self.assertEqual(Parser.recursivemult(eq), '2+2+144+2')

    def test_recurisvemult_all_operations(self):
        eq = "2*8*2+4/4-3"
        self.assertEqual(Parser.recursivemult(eq), '32+1-3')
    
    def test_recurisvemult_only_multanddiv2(self):
        eq = "2*8+4/4"
        self.assertEqual(Parser.recursivemult(eq), '16+1')

    def test_recurisvemult_div_addition_after(self):
        eq = "4/4+5"
        self.assertEqual(Parser.recursivemult(eq), '1+5')

    

    def test_recursiveadd(self):
        eq = "32+1-3"
        self.assertEqual(Parser.recursiveadd(eq), '30')

    def test_recursiveadd_onlyadd(self):
        eq = "32+1"
        self.assertEqual(Parser.recursiveadd(eq), '33')

    def test_recursiveadd_subtract_then_add(self):
        eq = "32-1+3"
        self.assertEqual(Parser.recursiveadd(eq), '34')

    def test_catching_negative_numbers(self):
        with self.assertRaises(Exception) as context:
            Parser.recursiveadd('4-8')

        self.assertTrue('Sorry, this produced a negative number! Not what this calculator is for!' in str(context.exception))


        

    #integration tests
    def test_integration_onlyadd(self):
        eq = "2+2"
        self.assertEqual(Helper.integration(eq), '4')

    def test_integration_add_and_sub(self):
        eq = "2+2-4"
        self.assertEqual(Helper.integration(eq), '0')

    def test_integration_add_and_sub_and_mult(self):
        eq = "2*2+2-2"
        self.assertEqual(Helper.integration(eq), '4')

    def test_integration_with_spacing(self):
        eq = "2/2 + 4 - 2 + 2*2"
        self.assertEqual(Helper.integration(eq), '7')

    def test_catching_negative_numbers_integration(self):
        with self.assertRaises(Exception) as context:
            Helper.integration('2*2-8*8')

        self.assertTrue('Sorry, this produced a negative number! Not what this calculator is for!' in str(context.exception))


if __name__ == '__main__':
    unittest.main()