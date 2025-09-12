import tensorflow as tf

# Example code for working with tf.nest module

# Create a nested structure
nested_structure = {
    'a': [1, 2, 3],
    'b': (4, 5),
    'c': {'d': 6, 'e': 7}
}

# Flatten the nested structure
flattened = tf.nest.flatten(nested_structure)
print("Flattened structure:", flattened)

# Pack the flattened structure back into the original nested structure
packed_structure = tf.nest.pack_sequence_as(nested_structure, flattened)
print("Packed structure:", packed_structure)

# Map a function over the nested structure
incremented_structure = tf.nest.map_structure(lambda x: x + 1, nested_structure)
print("Incremented structure:", incremented_structure)

# Assert same structure
tf.nest.assert_same_structure(nested_structure, incremented_structure)

# List the fields or keys for each level of the nested structure
for path_tuple in tf.nest.yield_flat_paths(nested_structure):
    print("Path:", path_tuple)

# Return True if the two structures have the same keys, sequences and named keys
is_same_structure = tf.nest.is_same_structure(nested_structure, incremented_structure)
print("Is same structure:", is_same_structure)
