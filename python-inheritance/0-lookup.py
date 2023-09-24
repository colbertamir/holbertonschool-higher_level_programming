#!/usr/bin/python3

def lookup(obj):

    attributes_and_methods = dir(obj)

    return attributes_and_methods


class MyClass1(object):
    pass


class MyClass2(object):
    my_attr1 = 3

    def my_meth(self):
        pass


print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(int))
