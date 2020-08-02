# Zadanie grupowe nr1
# Dobór w pary. Każda osoba wykonuje samodzielnie zadanie.
# Napisz dwie klasy o odpowiednich nazwach
# oblicza pierwiastek kwadratowy z: sumy zadanego jako argument ciągu liczb, podzielonej przez iloczyn tego ciągu
# wyznacza medianę liczb, wymnożoną przez połowę PI i na końcu zwiększoną o stałą Epsilon

from statistics import median
from numpy import prod
import math
import sys
import unittest


class ComplexMathOperations:

    @staticmethod
    def sqrt_of_sum_by_product(numbers: tuple) -> float:
        try:
            return math.sqrt(sum(numbers) / prod(numbers))
        except ZeroDivisionError:
            print("Cannot devide by 0")

    @staticmethod
    def median_multiply_pi_add_epsilon(numbers: tuple) -> float:
        return (median(numbers) * 0.5 * math.pi) + sys.float_info.epsilon


class MathTestCase(unittest.TestCase):
    positive_numbers = (2, 3, -5, 0, 7, 8, 9)

    def test_none(self):
        self.assertIsNotNone(ComplexMathOperations.sqrt_of_sum_by_product(self.positive_numbers))
        self.assertIsNotNone(ComplexMathOperations.median_multiply_pi_add_epsilon(self.positive_numbers))

    def test_is_not_negative(self):
        self.assertGreaterEqual(ComplexMathOperations.sqrt_of_sum_by_product(self.positive_numbers), 0,
                                "Cannot be negative")

    def test_smth
if __name__ == '__main__':
    unittest.main()
    # def test_is_equal_zero(self):
    #     self.assertEqual("dobra robota", multiplication(0, 0, 0))
    #
    # def test_is_equal_negative(self):
    #     self.assertEqual("dobra robota", multiplication(-1, 5, -5))
    #
    # def test_is_not_equal(self):
    #     self.assertNotEqual("zle", multiplication(2, 5, 10))