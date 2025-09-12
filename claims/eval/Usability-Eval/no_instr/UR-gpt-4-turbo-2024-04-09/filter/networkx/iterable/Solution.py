import networkx as nx

def is_iterable_with_len(obj):
    try:
        iter(obj)  # Check if it's iterable
        len(obj)   # Check if it has a well-defined length
        return True
    except (TypeError, AttributeError):
        return False

# Example usage
result = is_iterable_with_len([1, 2, 3])  # Should return True
print(f"Is [1, 2, 3] iterable with a well-defined len()? {result}")

result = is_iterable_with_len(5)  # Should return False
print(f"Is 5 iterable with a well-defined len()? {result}")
