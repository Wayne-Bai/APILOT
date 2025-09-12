import tensorflow as tf

# Define the input tensor
input_tensor = tf.placeholder(tf.float32, shape=[None, 1, 1, 1])

# Define the quantized tensor
quantized_tensor = tf.raw_ops.QuantizeAndDequantizeV4(input_tensor, is_training=False)

# Define the gradient of QuantizeAndDequantizeV4
gradient = tf.raw_ops.QuantizeAndDequantizeV4_Gradient(quantized_tensor, input_tensor, is_training=False)

# Print the gradient
print(gradient)
