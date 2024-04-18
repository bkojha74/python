'''
__str__() is used to return a human-readable string representation of an object
and is typically called by the str() function or when using print().

__repr__() returns an unambiguous string representation of the object
and is called by the repr() function or when using the interactive interpreter.
'''

class MyClass:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return f'MyClass({self.value})'
    def __str__(self):
        return f'MyClass instance with value {self.value}'

obj = MyClass(42)
print(obj)  # Output from __str__(): MyClass instance with value 42
repr_obj = repr(obj)
print(repr_obj)  # Output from __repr__(): MyClass(42)
