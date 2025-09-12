
import tensorflow as tf

# Define the input tensor and indices
input_tensor = tf.ragged.constant([[1, 2], [3], [4, 5, 6]])
indices = [0, 2]

# Use the Gather operation to gather slices from the input tensor according to the indices
output_tensor = tf.gather(input_tensor, indices, axis=0)

print(output_tensor)  # [[1, 2], [4, 5, 6]]
