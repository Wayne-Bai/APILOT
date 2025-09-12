
import networkx as nx

def is_iterable_with_defined_len(obj):
    try:
        len(obj)
        iter(obj)
        return True
    except TypeError:
        return False

# Test the function
obj1 = [1, 2, 3]
obj2 = "Hello"
obj3 = 100

print(is_iterable_with_defined_len(obj1))  # True
print(is_iterable_with_defined_len(obj2))  # True
print(is_iterable_with_defined_len(obj3))  # False
