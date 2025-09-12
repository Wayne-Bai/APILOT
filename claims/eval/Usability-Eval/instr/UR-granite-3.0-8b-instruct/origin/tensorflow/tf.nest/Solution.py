import tensorflow as tf

def flatten(nested):
    """Flatten a nested structure."""
    return tf.nest.flatten(nested)

def pack_sequences(sequences):
    """Pack a list of sequences into a single tensor."""
    return tf.nest.pack_sequence_as(sequences[0], sequences)

def map_structure(func, structure):
    """Apply a function to each element of a nested structure."""
    return tf.nest.map_structure(func, structure)

def unnest(nested):
    """Unnest a nested structure."""
    return tf.nest.unnest(nested)

def assert_same_structure(structure1, structure2):
    """Assert that two structures have the same structure."""
    return tf.nest.assert_same_structure(structure1, structure2)
