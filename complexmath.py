# Zadanie grupowe nr1
# Dobór w pary. Każda osoba wykonuje samodzielnie zadanie.
# Napisz dwie klasy o odpowiednich nazwach
# oblicza pierwiastek kwadratowy z: sumy zadanego jako argument ciągu liczb, podzielonej przez iloczyn tego ciągu
# wyznacza medianę liczb, wymnożoną przez połowę PI i na końcu zwiększoną o stałą Epsilon

from statistics import StatisticsError
from statistics import median
from numpy import prod  # zmienić na math
import unittest
import math
import sys


class MyExeption(Exception):  # zmienić nazwę

    def __init__(self, *args):
        if args:
            self._message = args[0]
        else:
            self._message = None

    def __str__(self):
        if self._message:
            return self._message
        else:
            return "Cannot find a square root of a negative number or divide by 0."


class ComplexMathOperations:

    @staticmethod
    def sqrt_of_sum_by_product(numbers: tuple) -> float:
        if 0 in numbers:
            raise MyExeption
        operation = sum(numbers) / prod(numbers)  # przejść jedną pętlę
        if operation < 0:
            raise MyExeption
        return float("{:.3f}".format(math.sqrt(operation)))

    @staticmethod
    def median_multiply_add(numbers: tuple) -> float:
        if not numbers:
            raise StatisticsError('no median for empty data')
        return float("{:.3f}".format(median(numbers) * 0.5 * math.pi + sys.float_info.epsilon))


class MyTestCase(unittest.TestCase):  # zmieniń nazwę na TestComplexMathOperstions i podzielić testowanie na dwie metody dla wyjątków osobno + wyrzucić testcase do osobnego pliku
    def test_sqrt(self):
        with self.assertRaises(MyExeption) as context:
            ComplexMathOperations.sqrt_of_sum_by_product((3, -5, 7, -8, 0, 9))
            ComplexMathOperations.sqrt_of_sum_by_product((3, -5, 7, 8, 4, 9))

        self.assertTrue('Cannot find a square root of a negative number or divide by 0.' in str(context.exception))
        self.assertEqual(ComplexMathOperations.sqrt_of_sum_by_product((2, 1, -5, 7, -8, 9)), 0.035)
        self.assertEqual(ComplexMathOperations.sqrt_of_sum_by_product((-9, -5, -10, 3)), 0.125)

    def test_median(self):
        with self.assertRaises(StatisticsError) as context:
            ComplexMathOperations.median_multiply_add(())

        self.assertTrue('no median for empty data' in str(context.exception))
        self.assertEqual(ComplexMathOperations.median_multiply_add((2, 3, -5, 0, 7, 8, 9)), 4.712)
        self.assertEqual(ComplexMathOperations.median_multiply_add((0, )), 0.0)
        self.assertEqual(ComplexMathOperations.median_multiply_add((-1,)), -1.571)


if __name__ == '__main__':
    unittest.main()
    
