# Zadanie grupowe nr1
# Dobór w pary. Każda osoba wykonuje samodzielnie zadanie.
# Napisz dwie klasy o odpowiednich nazwach
# oblicza pierwiastek kwadratowy z: sumy zadanego jako argument ciągu liczb, podzielonej przez iloczyn tego ciągu
# wyznacza medianę liczb, wymnożoną przez połowę PI i na końcu zwiększoną o stałą Epsilon

from statistics import StatisticsError
from statistics import median
from numpy import prod
import unittest
import math
import sys


class ComplexMathOperations:

    @staticmethod
    def sqrt_of_sum_by_product(numbers: tuple) -> float:
        if prod(numbers) <= 0:
            raise ValueError('cannot find sqrt of a negative number or divide by 0')
        return float("{:.3f}".format(math.sqrt(sum(numbers) / prod(numbers))))

    @staticmethod
    def median_multiply_add(numbers: tuple) -> float:
        if not numbers:
            raise StatisticsError('no median for empty data')
        return float("{:.3f}".format((median(numbers) * 0.5 * math.pi) + sys.float_info.epsilon))


class MyTestCase(unittest.TestCase):
    def test_sqrt(self):
        with self.assertRaises(ValueError) as context:
            ComplexMathOperations.sqrt_of_sum_by_product((3, -5, 7, -8, 0, 9))
            ComplexMathOperations.sqrt_of_sum_by_product((3, -5, 7, 8, 4, 9))

        self.assertTrue('cannot find sqrt of a negative number or divide by 0' in str(context.exception))
        self.assertEqual(ComplexMathOperations.sqrt_of_sum_by_product((2, 3, -5, 7, -8, 9)), 0.023)
        self.assertEqual(ComplexMathOperations.sqrt_of_sum_by_product(()), 0.0)

    def test_median(self):
        with self.assertRaises(StatisticsError) as context:
            ComplexMathOperations.median_multiply_add(())

        self.assertTrue('no median for empty data' in str(context.exception))
        self.assertEqual(ComplexMathOperations.median_multiply_add((2, 3, -5, 0, 7, 8, 9)), 4.712)
        self.assertEqual(ComplexMathOperations.median_multiply_add((0, )), 0.0)
        self.assertEqual(ComplexMathOperations.median_multiply_add((-1,)), -1.571)


if __name__ == '__main__':
    unittest.main()
