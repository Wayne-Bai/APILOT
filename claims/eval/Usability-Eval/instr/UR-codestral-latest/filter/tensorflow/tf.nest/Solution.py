import tensorflow as tf

# Let's assume we have a nested structure of tensors
nested = (tf.constant([1, 2]), [tf.constant([3, 4]), tf.constant([5, 6])])

# We can flatten the structure
flat = tf.nest.flatten(nested)
print('Flattened:', flat)

# And we can pack it back
packed = tf.nest.pack_sequence_as(nested, flat)
print('Packed:', packed)
