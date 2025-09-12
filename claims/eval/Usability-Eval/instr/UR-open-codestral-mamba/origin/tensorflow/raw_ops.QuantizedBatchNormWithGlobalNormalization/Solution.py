# Import TensorFlow module
import tensorflow as tf

# Create the input tensor
input_tensor = tf.constant([[[0.0, 1.0, 2.0], [3.0, 4.0, 5.0]]])

# Create scale tensor
scale_tensor = tf.constant([[[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]])

# Create offset tensor
offset_tensor = tf.constant([[[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]])

# Apply Quantized Batch Normalization
output_tensor = tf.nn.batch_normalization(input_tensor, offset_tensor, scale_tensor, None, None, 0.0)

print(output_tensor)
