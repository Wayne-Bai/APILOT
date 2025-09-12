import tensorflow as tf

# Define a function to flatten a nested structure
def flatten(nested_structure):
    return tf.nest.flatten(nested_structure)

# Define a function to unflatten a nested structure
def unflatten(flat_structure, original_structure):
    return tf.nest.pack_sequence_as(original_structure, flat_structure)

# Define a function to map a function over a nested structure
def map_structure(func, structure):
    return tf.nest.map_structure(func, structure)

# Define a function to reduce a nested structure
def reduce_structure(func, structure, initial_value=None):
    return tf.nest.reduce(func, structure, initial_value)
