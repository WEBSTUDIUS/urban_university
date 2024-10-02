from Module_6 import animals
import inspect
import sys


def introspection_info(obj):
    if isinstance(obj, (int, float, bool, str, list, tuple)):
        print(f"Input must be an instance of class. Got {type(obj)} ")
        return obj

    print("Type: ", type(obj))
    print("Class: ", obj.__class__)
    print("All attrs and methods: ", obj.__dir__())
    print("Attrs Only: ", vars(obj))
    print("Methods Only: ", [m[0] for m in inspect.getmembers(obj, predicate=inspect.ismethod)])
    print("Module: ", obj.__module__)
    print("Memory size: ", sys.getsizeof(obj))


object_1 = animals.Animal('Python')
introspection_info(object_1)
introspection_info(123)
