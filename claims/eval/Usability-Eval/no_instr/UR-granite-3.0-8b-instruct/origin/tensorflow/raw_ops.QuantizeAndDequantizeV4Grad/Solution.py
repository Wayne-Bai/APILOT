import tensorflow as tf

# Define the input tensor
input_tensor = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])

# Define the quantize and dequantize operation
quantize_and_dequantize = tf.raw_ops.QuantizeAndDequantizeV4(
    input_tensor,
    min_range=0.0,
    max_range=255.0,
    num_bits=8,
    narrow_range=False
)

# Compute the gradient of the quantize and dequantize operation
gradient = tf.gradients(quantize_and_dequantize, input_tensor)

print(gradient)
