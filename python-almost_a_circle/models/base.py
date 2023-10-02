<<<<<<< HEAD
#!/usr/bin/python3
"""Defines the Base class."""


class Base:
    """Base class for managing id attributes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes the Base class.

        Args:
            id (int, optional): An integer identifier. If provided, it is assigned to
                the 'id' attribute. If not provided or 'None', a new
                'id' is created by incrementing the class-level '__nb_objects' counter.

        Returns:
            None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
=======
#!/usr/bin/python3
"""Defines the Base class"""


class Base:
    """Base class for managing id attributes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes an instance of the Base class.

        Args:
            id (int, optional): Is an integer identifier.
            If provided, it is assigned to
            the 'id' attribute. If 'None' is passed, a new 'id'
            is created by incrementing the '__nb_objects' counter.

        Returns:
            None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
>>>>>>> 5706e1135180e2ffe73b5cddd0fbe188eb4bfd83
