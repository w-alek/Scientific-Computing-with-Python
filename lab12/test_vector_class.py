import unittest
from math import sqrt
from vector_class import Vector


class TestVector(unittest.TestCase):

    def setUp(self):
        print('Prepare two vectors A and B')
        self.vecA = Vector(1, 2, 3)
        self.vecB = Vector(2, -3, 2)

    def test_not_equal(self):
        self.assertNotEqual(self.vecA, self.vecB)

    def test_addition(self):
        self.assertEqual(self.vecA + self.vecB, Vector(3, -1, 5))

    def test_difference(self):
        self.assertEqual(self.vecA - self.vecB, Vector(-1, 5, 1))

    def test_dot_product(self):
        self.assertEqual(self.vecA * self.vecB, 2)

    def test_cross_product(self):
        self.assertEqual(self.vecA.cross(self.vecB), Vector(13, 4, -7))

    def test_length(self):
        self.assertEqual(self.vecA.length(), sqrt(14))

    def test_set_vec(self):
        self.assertEqual(len(set([self.vecA, self.vecA, self.vecB])), 2)

    def tearDown(self):
        print("cleaning")
        pass


if __name__ == "__main__":
    unittest.main()
