import unittest
from geometric_lib.square import area, perimeter

class SquareTestCase(unittest.TestCase):

    def test_area_normal(self):
        self.assertEqual(area(5), 25)

    def test_area_normal_2(self):
        self.assertEqual(area(2), 4)

    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            area(-4)

    def test_perimeter_normal(self):
        self.assertEqual(perimeter(7), 28)

    def test_perimeter_normal_2(self):
        self.assertEqual(perimeter(3), 12)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            perimeter(-8)