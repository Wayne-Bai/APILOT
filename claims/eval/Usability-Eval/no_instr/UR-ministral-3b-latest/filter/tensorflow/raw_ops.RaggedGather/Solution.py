import tensorflow as tf

# Define the rank and shape of the parameters tensor
rank = 2
params_shape = [tf.constant([[10]]), tf.constant([10])]

# Create the parameters tensor
params = tf.ragged.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Indices tensor
indices = tf.constant([[0, 1, 2]])

# Gather ragged slices from params axis 0 according to indices
gathered = tf.raw_ops.GatherV2(input=params, indices=indices)

print(gathered)
