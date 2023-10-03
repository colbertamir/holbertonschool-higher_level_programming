#!/usr/bin/python3
"""Defines class Student."""


class Student:
    """Represents student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name: The first name of the student.
            last_name: The last name of the student.
            age: The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary version Student.

        If attrs is a list of strings, represents only those attrs
        included in list.

        Args:
            attrs: The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__