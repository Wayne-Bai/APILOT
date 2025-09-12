import tensorflow as tf

# Define a tensor
tensor = tf.constant([[1, 2, 3], [4, 5, 6]])

# Define the number of times to tile
num_times = 2

# Tile the tensor
tilled_tensor = tf.tile(tensor, [num_times, num_times])

# Print the tilled tensor
print(tilled_tensor)
