import tensorflow as tf

# Define a simple variable
x = tf.Variable([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=tf.float32)

# Define the indices for gathering
indices = [[0, 0], [1, 1], [2, 2]]

# Gather slices from the variable `x` based on the defined indices
y = tf.raw_ops.Gather(params=x, indices=indices)

# Print the result
print(y)
