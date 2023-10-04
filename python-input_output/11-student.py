#!/usr/bin/python3
"""Defines class Student."""


class Student:
    """Represents student."""

    def __init__(self, first_name, last_name, age):
        """Initializes new Student.

        Args:
            first_name (str): The first name of student.
            last_name (str): The last name of student.
            age (int): The age of student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary version of Student.

        If attrs is a list of strings, represents only those attrs
        in the list.

        Args:
            attrs (list): The attributes to represent.
        """
        if attrs is None:
            return self.__dict__
        return {k: v for k, v in self.__dict__.items() if k in attrs}

    def reload_from_json(self, json):
        """Replace all attributes of Student.

        Args:
            json (dict): The key/value pairs replacing attributes.
        """
        for k, v in json.items():
            setattr(self, k, v)
