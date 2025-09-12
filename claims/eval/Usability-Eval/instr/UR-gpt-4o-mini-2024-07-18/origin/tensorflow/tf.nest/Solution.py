import tensorflow as tf

def flatten_nested_structure(nested):
    """Flatten a nested structure into a flat list."""
    flat_list = []

    def recursive_flatten(nested_item):
        if isinstance(nested_item, (list, tuple)):
            for item in nested_item:
                recursive_flatten(item)
        else:
            flat_list.append(nested_item)

    recursive_flatten(nested)
    return flat_list

# Example usage
nested_structure = [[1, 2, 3], [4, [5, 6]], 7]
flat_result = flatten_nested_structure(nested_structure)
print(flat_result)  # Output: [1, 2, 3, 4, 5, 6, 7]
