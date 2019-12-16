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
        expected_value = 1
        calculated_value = nr.factrl(1)
        self.assertEqual(calculated_value, expected_value)

        expected_value = 120
        calculated_value = nr.factrl(5)
        self.assertEqual(calculated_value, expected_value)

        expected_value = np.math.factorial(10)
        calculated_value = nr.factrl(10)
        self.assertEqual(calculated_value, expected_value)

        expected_value = np.math.factorial(15)
        calculated_value = nr.factrl(15)
        self.assertEqual(calculated_value, expected_value)

        expected_value = np.math.factorial(20)
        calculated_value = nr.factrl(20)
        self.assertEqual(calculated_value, expected_value)
