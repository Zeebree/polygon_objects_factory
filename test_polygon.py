import unittest

from polygon import Polygon


class TestConstruction(unittest.TestCase):

    def test_polygon_creation(self):
        t = Polygon(3, 9.2)

    def test_negative_circumradius(self):
        with self.assertRaises(ValueError):
            t = Polygon(3, -3.2)

    def test_less_than_three_edges(self):
        with self.assertRaises(ValueError):
            t = Polygon(2, 4.4)


class TestPropertiesTriangle(unittest.TestCase):

    def setUp(self):
        n = 3
        circumradius = 9
        self.triangle = Polygon(n, circumradius)

    def test_number_of_vertices(self):
        self.assertTrue(self.triangle.number_of_vertices == 3)

    def test_number_of_edges(self):
        self.assertTrue(self.triangle.number_of_edges == 3)

    def test_circumradius(self):
        self.assertTrue(self.triangle.circumradius == 9)

    def test_edge_length(self):
        self.assertAlmostEqual(self.triangle.edge_length, 15.5885, delta=0.01)

    def test_apothem(self):
        self.assertAlmostEqual(self.triangle.apothem, 4.5, delta=0.01)

    def test_area(self):
        self.assertAlmostEqual(self.triangle.area, 105.2, delta=0.1)

    def test_perimeter(self):
        self.assertAlmostEqual(self.triangle.perimeter, 46.7654, delta=0.01)

    def test_interior_angle(self):
        self.assertAlmostEqual(self.triangle.interior_angle, 60, delta=0.01)


class TestComparePolygons(unittest.TestCase):

    def setUp(self):
        self.triangle = Polygon(3, 7)
        self.triangle2 = Polygon(3, 7)
        self.triangle3 = Polygon(3, 77)
        self.hexagon = Polygon(6, 11)

    def test_positive_equality(self):
        self.assertTrue(self.triangle == self.triangle2)

    def test_negative_equality(self):
        self.assertFalse(self.triangle == self.triangle3)

    def test_positive_inequality(self):
        self.assertTrue(self.triangle != self.triangle3)

    def test_negative_inequality(self):
        self.assertFalse(self.triangle != self.triangle2)

    def test_gt_positive(self):
        self.assertTrue(self.hexagon > self.triangle)

    def test_gt_negative(self):
        self.assertFalse(self.triangle > self.hexagon)

    def test_lt_positive(self):
        self.assertTrue(self.triangle < self.hexagon)

    def test_lt_negative(self):
        self.assertFalse(self.hexagon < self.triangle)


if __name__ == '__main__':
    unittest.main()