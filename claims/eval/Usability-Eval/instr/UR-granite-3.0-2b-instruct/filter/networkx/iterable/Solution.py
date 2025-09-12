import networkx as nx

def is_iterable_with_len(obj):
    return hasattr(obj, '__len__')

# Test the function
obj1 = [1, 2, 3]
obj2 = ('a', 'b', 'c')
obj3 = (1, 2, 3, 4, 5)

print(is_iterable_with_len(obj1))  # True
print(is_iterable_with_len(obj2))  # True
print(is_iterable_with_len(obj3))  # True

obj4 = 123
obj5 = None

print(is_iterable_with_len(obj4))  # False
print(is_iterable_with_len(obj5))  # False
