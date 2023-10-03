import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{'key': 'value'}]),
                         '[{"key": "value"}]')

    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        json_str = '[{"key": "value"}]'
        self.assertEqual(Base.from_json_string(json_str), [{'key': 'value'}])

    def test_create(self):
        rect_dict = {'id': 1, 'width': 2, 'height': 3, 'x': 4, 'y': 5}
        square_dict = {'id': 6, 'size': 7, 'x': 8, 'y': 9}
        rect_obj = Rectangle.create(**rect_dict)
        square_obj = Rectangle.create(**square_dict)
        self.assertTrue(isinstance(rect_obj, Rectangle))
        self.assertTrue(isinstance(square_obj, Rectangle))


if __name__ == "__main__":
    unittest.main()
