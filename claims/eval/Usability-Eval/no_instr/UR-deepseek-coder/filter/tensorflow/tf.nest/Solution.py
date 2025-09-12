import tensorflow as tf

def flatten_nested_structure(structure):
    """
    Flattens a nested structure into a list of its elements.

    Args:
        structure: A nested structure of lists, tuples, or dictionaries.

    Returns:
        A list of elements from the nested structure.
    """
    if isinstance(structure, (list, tuple)):
        result = []
        for item in structure:
            result.extend(flatten_nested_structure(item))
        return result
    elif isinstance(structure, dict):
        result = []
        for key, value in structure.items():
            result.extend(flatten_nested_structure(value))
        return result
    else:
        return [structure]

def pack_into_nested_structure(elements, structure):
    """
    Packs a list of elements into a nested structure.

    Args:
        elements: A list of elements to be packed.
        structure: The target nested structure (list, tuple, or dictionary).

    Returns:
        The nested structure filled with the elements.
    """
    if isinstance(structure, list):
        return [pack_into_nested_structure(elements, sub_structure) for sub_structure in structure]
    elif isinstance(structure, tuple):
        return tuple(pack_into_nested_structure(elements, sub_structure) for sub_structure in structure)
    elif isinstance(structure, dict):
        return {key: pack_into_nested_structure(elements, value) for key, value in structure.items()}
    else:
        return elements.pop(0) if elements else None

def map_structure(func, structure):
    """
    Applies a function to each element in a nested structure.

    Args:
        func: The function to apply.
        structure: The nested structure to map over.

    Returns:
        A new nested structure with the function applied to each element.
    """
    if isinstance(structure, (list, tuple)):
        return type(structure)(map_structure(func, item) for item in structure)
    elif isinstance(structure, dict):
        return {key: map_structure(func, value) for key, value in structure.items()}
    else:
        return func(structure)

def assert_same_structure(structure1, structure2):
    """
    Asserts that two nested structures have the same structure.

    Args:
        structure1: The first nested structure.
        structure2: The second nested structure.

    Raises:
        ValueError: If the structures do not have the same structure.
    """
    if isinstance(structure1, (list, tuple)) and isinstance(structure2, (list, tuple)):
        if len(structure1) != len(structure2):
            raise ValueError("Structures have different lengths.")
        for item1, item2 in zip(structure1, structure2):
            assert_same_structure(item1, item2)
    elif isinstance(structure1, dict) and isinstance(structure2, dict):
        if set(structure1.keys()) != set(structure2.keys()):
            raise ValueError("Structures have different keys.")
        for key in structure1:
            assert_same_structure(structure1[key], structure2[key])
    elif type(structure1) != type(structure2):
        raise ValueError("Structures have different types.")

# Example usage:
# nested_structure = [1, (2, {'a': 3, 'b': [4, 5]})]
# flattened = flatten_nested_structure(nested_structure)
# print(flattened)  # Output: [1, 2, 3, 4, 5]
# packed = pack_into_nested_structure(flattened, nested_structure)
# print(packed)  # Output: [1, (2, {'a': 3, 'b': [4, 5]})]
# mapped = map_structure(lambda x: x * 2, nested_structure)
# print(mapped)  # Output: [2, (4, {'a': 6, 'b': [8, 10]})]
# assert_same_structure(nested_structure, [1, (2, {'a': 3, 'b': [4, 5]})])  # No error
