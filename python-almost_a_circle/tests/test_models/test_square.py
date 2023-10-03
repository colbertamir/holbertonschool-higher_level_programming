import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_initialization(self):
        s = Square(3, 2, 4, 5)
        self.assertEqual(s.id, 5)
        self.assertEqual(s.size, 3)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 4)

    def test_area(self):
        s = Square(3)
        self.assertEqual(s.area(), 9)

    def test_str(self):
        s = Square(4, 1, 2, 6)
        expected_output = "[Square] (6) 1/2 - 4"
        self.assertEqual(str(s), expected_output)

    def test_size_property(self):
        s = Square(2)
        self.assertEqual(s.size, 2)
        s.size = 5
        self.assertEqual(s.size, 5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)

    def test_update(self):
        s = Square(2)
        s.update(7, 4, 1, 3)
        self.assertEqual(s.id, 7)
        self.assertEqual(s.size, 4)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 3)

    def test_to_dictionary(self):
        s = Square(3, 2, 1, 4)
        expected_dict = {"id": 4, "size": 3, "x": 2, "y": 1}
        self.assertEqual(s.to_dictionary(), expected_dict)


if __name__ == "__main__":
    unittest.main()
