#!/usr/bin/python3
"""Defines a base model class."""
import json
import csv


class Base:
    """Base class.

    Private Class Attributes:
        __nb_objects (int): Number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a Base.

        Args:
            id (int): The id of Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON version of a list of dicts.

        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        return json.dumps(list_dictionaries) if list_dictionaries else "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON representation of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".json"
        list_dicts = [o.to_dictionary() for o in list_objs] \
            if list_objs else []
        with open(filename, "w") as jsonfile:
            jsonfile.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the deserialization of a JSON string.

        Args:
            json_string (str): A JSON string version of a list of dicts.
        Returns:
            If json_string is None or empty - empty list.
            Otherwise - the Python list represented by json_string.
        """
        return json.loads(json_string) if json_string else []

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantied from a dictionary of attributes.

        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        new = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings.

        Reads from `<cls.__name__>.json`.

        Returns:
            If the file doesn't exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV version of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        fieldnames = ["id", "width", "height", "x", "y"] \
            if cls.__name__ == "Rectangle" else ["id", "size", "x", "y"]
        list_dicts = [obj.to_dictionary() for obj in list_objs] \
            if list_objs else []
        with open(filename, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(list_dicts)

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.

        Reads from `<cls.__name__>.csv`.

        Returns:
            If the file doesn't exist - a empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        fieldnames = ["id", "width", "height", "x", "y"] \
            if cls.__name__ == "Rectangle" else ["id", "size", "x", "y"]
        try:
            with open(filename, "r", newline="") as csvfile:
                list_dicts \
                    = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = \
                    [dict((k, int(v)) for k, v in d.items())
                     for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []
