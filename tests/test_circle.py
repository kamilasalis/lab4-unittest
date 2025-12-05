import unittest
import math
from geometric_lib.circle import area, perimeter

class CircleTestCase(unittest.TestCase):

    def test_area_normal(self):
        self.assertAlmostEqual(area(10), math.pi * 100)

    def test_area_normal_2(self):
        self.assertAlmostEqual(area(2), math.pi * 4)

    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            area(-8)

    def test_area_arguments(self):
        with self.assertRaises(TypeError):
            area('a')


    def test_perimeter_normal(self):
        self.assertAlmostEqual(perimeter(5), 2 * math.pi * 5)

    def test_perimeter_normal_2(self):
        self.assertAlmostEqual(perimeter(2), 2 * math.pi * 2)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            perimeter(-10)
    def test_perimeter_arguments(self):
        with self.assertRaises(TypeError):
            perimeter('a')
