
import tensorflow as tf

# Create a variable for the input tensor
input_tensor = tf.constant([[1, 2, 3], [4, 5, 6]])

# Quantize the input tensor
quantized_tensor = tf.raw_ops.Quantize(
    input=input_tensor,
    axis=None,
    is_ascending=False,
    is_unsigned=True
)

# Dequantize the quantized tensor
dequantized_tensor = tf.raw_ops.Dequantize(
    input=quantized_tensor,
    axis=None,
    is_ascending=False,
    is_unsigned=True
)
