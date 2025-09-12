import tensorflow as tf

# Assuming that 'input_tensor' is the given tensor
input_tensor = tf.constant([1, 2, 3])

# Repeating the tensor 3 times along the 0-axis
output_tensor = tf.tile(input_tensor, [3])

print(output_tensor)
