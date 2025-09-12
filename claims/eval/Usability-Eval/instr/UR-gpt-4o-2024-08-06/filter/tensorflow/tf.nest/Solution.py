import tensorflow as tf

# Creating a nested structure
nested_structure = {'a': [1, 2, 3], 'b': (4, 5)}

# Flatten the nested structure to a flat list
flattened_structure = tf.nest.flatten(nested_structure)
print("Flattened structure:", flattened_structure)

# Pack a flat sequence to a nested structure
packed_structure = tf.nest.pack_sequence_as(nested_structure, flattened_structure)
print("Packed structure:", packed_structure)

# Map a function over each element of the nested structure
mapped_structure = tf.nest.map_structure(lambda x: x * 2, nested_structure)
print("Mapped structure:", mapped_structure)

# Assert two nested structures are the same
nested_structure_2 = {'a': [1, 2, 3], 'b': (4, 5)}
tf.nest.assert_same_structure(nested_structure, nested_structure_2)

print("Both structures have the same shape")
