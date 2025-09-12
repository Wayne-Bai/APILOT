import tensorflow as tf

# Let's assume we have a nested dictionary
nested = {'a': {'b': [1, 2, 3], 'c': 'hello'}, 'd': [4, 5, 6]}

# We can flatten the dictionary using tf.nest.flatten
flat_nested = tf.nest.flatten(nested)
print("Flattened nested dictionary: ", flat_nested)

# And we can create a structure of nested dictionaries out of the flattened list
structured_nested = tf.nest.pack_sequence_as(nested, flat_nested)
print("Structured nested dictionary: ", structured_nested)
