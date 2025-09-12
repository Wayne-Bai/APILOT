
import networkx as nx

def is_iterator(obj):
    return hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes))

# Testing the function
obj1 = [1, 2, 3]
obj2 = "Hello"
obj3 = {1: 'a', 2: 'b', 3: 'c'}

print(is_iterator(obj1))  # True
print(is_iterator(obj2))  # False
print(is_iterator(obj3))  # True
