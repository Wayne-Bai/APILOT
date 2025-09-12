import networkx as nx

def is_iterable_with_len(obj):
    try:
        len(obj)
        return True
    except TypeError:
        return False

# Test the function
print(is_iterable_with_len([1, 2, 3]))  # Expected output: True
print(is_iterable_with_len(123))  # Expected output: False
print(is_iterable_with_len('hello'))  # Expected output: True
