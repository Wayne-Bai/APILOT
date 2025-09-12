import tensorflow as tf

# A simple example of a nested structure
nested_structure = [tf.constant([1, 2, 3]), { "key": tf.constant(42) }]

# Using tf.nest.flatten to flatten the structure
flat_structure = tf.nest.flatten(nested_structure)

print("Original Nested Structure: ", nested_structure)
print("Flattened Structure: ", flat_structure)

# Now let's take the flattened structure and pack it back into the nested form
reconstructed_structure = tf.nest.pack_sequence_as(nested_structure, flat_structure)

print("Reconstructed Structure: ", reconstructed_structure)
