#!/usr/bin/python3

def lookup(obj):
    """
    Get a list of public attributes and methods of an object.

    Args:
        obj: The object being inspected

    Returns:
        A list of public attributes/method names
    """

    attributes_and_methods = dir(obj)

    filtered_attributes_and_methods \
        = [i for i in attributes_and_methods if not i.startswith("_")]

    return filtered_attributes_and_methods


class MyClass1(object):
    pass


class MyClass2(object):
    my_attr1 = 3

    def my_meth(self):
        pass


print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(int))
