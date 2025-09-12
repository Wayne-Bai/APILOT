import tensorflow as tf

def flatten_nested_structure(structure):
    """
    Flattens a nested structure into a list of its elements.

    Args:
        structure: A nested structure of lists, tuples, or dictionaries.

    Returns:
        A list containing all the elements from the nested structure.
    """
    return tf.nest.flatten(structure)

def pack_into_nested_structure(elements, structure):
    """
    Packs a list of elements into a nested structure.

    Args:
        elements: A list of elements to be packed.
        structure: The target nested structure (list, tuple, or dictionary).

    Returns:
        The nested structure filled with the provided elements.
    """
    return tf.nest.pack_sequence_as(structure, elements)

def map_structure(func, *structures):
    """
    Applies a function to each element in the nested structures.

    Args:
        func: The function to apply.
        *structures: One or more nested structures.

    Returns:
        A new nested structure with the function applied to each element.
    """
    return tf.nest.map_structure(func, *structures)

def assert_same_structure(structure1, structure2):
    """
    Asserts that two nested structures have the same structure.

    Args:
        structure1: The first nested structure.
        structure2: The second nested structure.

    Raises:
        ValueError: If the structures do not have the same structure.
    """
    tf.nest.assert_same_structure(structure1, structure2)

def is_nested(structure):
    """
    Checks if a structure is nested (contains lists, tuples, or dictionaries).

    Args:
        structure: The structure to check.

    Returns:
        True if the structure is nested, False otherwise.
    """
    return tf.nest.is_nested(structure)

# Example usage:
nested_structure = {'a': [1, 2], 'b': (3, {'c': 4})}
flattened = flatten_nested_structure(nested_structure)
print("Flattened structure:", flattened)

repacked = pack_into_nested_structure(flattened, nested_structure)
print("Repacked structure:", repacked)

mapped = map_structure(lambda x: x * 2, nested_structure)
print("Mapped structure:", mapped)

assert_same_structure(nested_structure, repacked)
print("Structures are the same.")

print("Is nested:", is_nested(nested_structure))
