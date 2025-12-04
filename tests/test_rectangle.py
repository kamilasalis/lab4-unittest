import unittest
from geometric_lib.rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):

    def test_area_normal(self):
        self.assertEqual(area(10, 5), 50)

    def test_area_normal_2(self):
        self.assertEqual(area(1, 2), 2)    

    def test_area_zero(self):
        self.assertEqual(area(10, 0), 0)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            area(-10, 5)

    def test_perimeter_normal(self):
        self.assertEqual(perimeter(10, 5), 30)

    def test_perimeter_normal_2(self):
        self.assertEqual(perimeter(1, 2), 6)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0, 5), 10)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            perimeter(10, -5)