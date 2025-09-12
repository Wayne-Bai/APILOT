import networkx as nx

def is_iterator(obj):
    try:
        _ = iter(obj)
        return True
    except TypeError:
        return False

# Testing the function
print(is_iterator([]))  # True
print(is_iterator({}))  # True
print(is_iterator(()))  # True
print(is_iterator('string'))  # True
print(is_iterator(123))  # False
