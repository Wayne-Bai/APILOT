import tensorflow as tf

# Define a tensor of input values
input_tensor = tf.constant([1, 2, 3, 4], dtype=tf.float32)

# Define the number of bits for the quantization
num_bits = 8

# Quantize the input tensor using the `QuantizeAndDequantizeV4` op
quantized_tensor = tf.raw_ops.QuantizeAndDequantizeV4(
    input=input_tensor,
    num_bits=num_bits,
    signed_input=True,
    range_given=False
)

# Compute the gradients of the quantized tensor using `QuantizeAndDequantizeV4Grad`
gradients = tf.raw_ops.QuantizeAndDequantizeV4Grad(
    input_gradients=tf.gradients(quantized_tensor, input_tensor),
    num_bits=num_bits,
    signed_input=True,
    range_given=False
)

# Print the gradients
print(gradients)
