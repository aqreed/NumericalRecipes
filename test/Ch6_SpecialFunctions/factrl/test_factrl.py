"""
    Unit tests of the factorial function

    Expected values extracted from Numpy Math
"""
import numericalrecipes as nr
import numpy as np
import unittest as ut


class Test_factrl_input(ut.TestCase):
    """
        Checks values
    """
    def test_negative_value(self):
        """
            Checks values x < 0
        """
        self.assertRaises(ValueError, nr.factrl, -1)

    def test_nonInteger_values(self):
        """
            Checks float, char, etc, values
        """
        self.assertRaises(TypeError, nr.factrl, 1.0)
        self.assertRaises(TypeError, nr.factrl, 'a')
        self.assertRaises(TypeError, nr.factrl, '[0, 1]')

    def test_fctrl(self):
        c1 = 1 - nr.factrl(1)
        c2 = 120 - nr.factrl(5)
        c3 = np.math.factorial(10) - nr.factrl(10)
        c4 = np.math.factorial(15) - nr.factrl(15)
        c5 = np.math.factorial(20) - nr.factrl(20)

        calculated_value = [c1, c2, c3, c4, c5]
        expected_value = [0, 0, 0, 0, 0]
        self.assertEqual(calculated_value, expected_value)
