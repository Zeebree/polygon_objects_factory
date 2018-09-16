"""
Polygon object factory
"""

import math
from fractions import Fraction


class Polygon:
    """
    Represent regular strictly convex polygon.
        - all interior angles are less than 180 degree.
        - all sides have equal length.
    """

    def __init__(self, n, circumradius):
        """
        Initialise polygon object.

        Args:
            n: number of edges/vertices of polygon.
            circumradius: positive float number which represent circumradius of polygon.

        Raises:
            ValueError: If 'n' is less than 3.
                        If 'circumradius' is negative number.
        """
        if n < 3:
            raise ValueError('Number of edges/vertices of polygon has to be greater or equal to 3')
        if circumradius < 0:
            raise ValueError('Circumradius of polygon has to be positive number')

        self._n = n     # n edges/vertices
        self._circumradius = circumradius   # R circumradius

    @property
    def number_of_vertices(self):
        """
        Return number of vertices.
        """
        return self._n

    @property
    def number_of_edges(self):
        """
        Return number of edges.
        """
        return self._n

    @property
    def circumradius(self):
        """
        Return circumradius.
        """

        return self._circumradius

    @property
    def edge_length(self):
        """
        Return edge length.
        """
        return 2 * self._circumradius * Fraction(math.sin(math.pi/self._n)).limit_denominator(100)    # s = 2R sin(PI/n)

    @property
    def apothem(self):
        """
        Return apothem.
        """
        return self._circumradius * Fraction(math.cos(math.pi/self._n))    # a = R cos(PI/n)

    @property
    def area(self):
        """
        Return area.
        """
        return 0.5 * self.number_of_edges * self.edge_length * self.apothem   # area = 1/2 n s a

    @property
    def perimeter(self):
        """
        Return perimeter.
        """
        return self.number_of_edges * self.edge_length  # perimeter = n s

    @property
    def interior_angle(self):
        """
        Return interior angle.
        """
        return (self.number_of_edges - 2) * 180 / self.number_of_edges

    def __eq__(self, other):
        """
        Test equality of two polygons.

        Args:
            other: object of Polygon type.

        Returns:
            'True' if respective number of vertices and circumradius of two polygons are the same,
            otherwise return 'False'.
        """
        if isinstance(other, self.__class__):
            # if number of vertices and circumradius are equal
            return self.number_of_edges == other.number_of_edges and self.circumradius == other.circumradius
        else:
            # Since a doesn't know how to compare with b, let's give b
            # a chance to compare itself with a.
            return NotImplemented

    def __gt__(self, other):
        """
        Test greater ordering of two polygons.

        Args:
            other: object of Polygon type.

        Returns:
            'True' if lhs 'self' object has greater number of vertices than 'other' object.
             Otherwise return 'False'.
        """
        if isinstance(other, self.__class__):
            # based on number of vertices   n = 4 > n = 3 True. What if has the same
            return self.number_of_edges > other.number_of_edges
        else:
            # Since a doesn't know how to compare with 'other', let's give 'other'
            # a chance to compare itself with a.
            return NotImplemented

    def __repr__(self):
        return "{0}({1}, {2})".format(self.__class__.__name__, self._n, self._circumradius)


if __name__ == '__main__':
    p = Polygon(3, 9.3)
    print(p)
    print("{0} has {1} edges.".format(p, p.number_of_edges))
    print("{0} has {1} vertices.".format(p, p.number_of_vertices))
    print("{0} has {1} circumradius.".format(p, p.circumradius))
    print("{0} has {1} edge length.".format(p, p.edge_length))
    print("{0} has {1} apothem.".format(p, p.apothem))
    print("{0} has {1} area.".format(p, p.area))
    print("{0} has {1} perimeter.".format(p, p.perimeter))
    print("{0} has {1} interior angle.".format(p, p.interior_angle))
    t1 = Polygon(3, 9.3)
    t2 = Polygon(3, 9.3)
    t3 = Polygon(3, 9.4)
    t4 = Polygon(4, 9.4)
    print("{0} == {1}: {2}".format(t1, t2, t1 == t2))
    print("{0} == {1}: {2}".format(t1, t3, t1 == t3))
    print("{0} > {1}: {2}".format(t1, t2, t1 > t2))
    print("{0} > {1}: {2}".format(t4, t1, t4 > t1))
    print("{0} < {1}: {2}".format(t1, t4, t1 < t4))
