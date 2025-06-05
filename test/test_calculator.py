import unittest

from src.calculator import suma, resta, multiplicacion, division

class CalculatorTest(unittest.TestCase):
   
    def test_sum(self):
        self.assertEqual(suma(2, 3), 5)

    def test_resta(self):
        self.assertEqual(resta(10, 5), 5)
    
    def test_multiplicacion(self):
        self.assertEqual(multiplicacion(10, 5), 50)
        
    def test_division(self):
        self.assertEqual(division(8, 2), 4)