from attr.validators import is_callable

from Module_6 import animals
import inspect


def introspection_info(obj):
    """
    This function prints out the type, memory address, and all the attributes of an object.
    """
    print("Type: ", type(obj))
    print("Class: ", obj.__class__)
    print("All attrs and methods: ", obj.__dir__())
    print("Attrs Only: ", vars(obj))
    print("Methods Only: ", [m[0] for m in inspect.getmembers(obj, predicate=inspect.ismethod)])
    print("Module: ", obj.__module__)



object_1 = animals.Animal('Python')
introspection_info(object_1)