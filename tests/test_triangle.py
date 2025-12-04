import unittest
from geometric_lib.triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):

    def test_area_normal(self):
        self.assertEqual(area(10, 6), 30)

    def test_area_normal_2(self):
        self.assertEqual(area(2,3), 3)

    def test_area_zero_height(self):
        self.assertEqual(area(10, 0), 0)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            area(-10, 5)

    def test_perimeter_normal(self):
        self.assertEqual(perimeter(3, 4, 5), 12)

    def test_perimeter_normal_2(self):
        self.assertEqual(perimeter(5,7,6), 18)

    def test_perimeter_zero_side(self):
        self.assertEqual(perimeter(0, 4, 5), 9)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            perimeter(3, -4, 5)