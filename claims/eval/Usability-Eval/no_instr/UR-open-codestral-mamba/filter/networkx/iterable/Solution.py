import networkx as nx

def is_iterable_and_length(obj):
    try:
        len(obj)
        return True
    except (TypeError, AttributeError):
        return False

# Testing the function with various inputs
print(is_iterable_and_length((1, 2, 3)))  # Expected output: True
print(is_iterable_and_length("asdf"))     # Expected output: True
print(is_iterable_and_length({1: "a", 2: "b"}))  # Expected output: True
print(is_iterable_and_length((i for i in range(3))))  # Expected output: True
print(is_iterable_and_length(123))        # Expected output: False
print(is_iterable_and_length(None))       # Expected output: False

