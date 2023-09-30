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
