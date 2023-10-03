import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_initialization(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.id, 5)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_area(self):
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test_display(self):
        r = Rectangle(2, 2)
        expected_output = "##\n##\n"
        with self.assertLogs(level='INFO') as logs:
            r.display()
        self.assertEqual(logs.output, [expected_output])

    def test_str(self):
        r = Rectangle(4, 5, 1, 2, 6)
        expected_output = "[Rectangle] (6) 1/2 - 4/5"
        self.assertEqual(str(r), expected_output)


if __name__ == "__main__":
    unittest.main()
