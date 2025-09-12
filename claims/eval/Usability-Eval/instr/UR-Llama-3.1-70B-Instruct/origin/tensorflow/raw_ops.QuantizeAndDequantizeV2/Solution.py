# Import necessary libraries
import tensorflow as tf
import numpy as np

# Create a simple tensor
tensor = tf.constant([0.5, 1.2, 3.4, 5.6, 6.7])

# Quantizes the tensor
quantized_tensor = tf.raw_ops.QuantizeV2(
    input=tensor,
    min_range=tf.constant(-10),
    max_range=tf.constant(10),
    T=tf.dtypes.dtypes.float32,
    mode="MIN_COMBINED",
    round_mode="HALF_TO_EVEN",
    narrow_range=False,
    axis=-1,
    name=None
)

# Dequantizes the tensor
dequantized_tensor = tf.raw_ops.Dequantize(
    input=quantized_tensor,
    min_range=tf.constant(-10),
    max_range=tf.constant(10),
    mode="MIN_COMBINED",
    narrow_range=False,
    axis=-1,
    name=None
)

# Print the result
print("Original tensor:", tensor)
print("Quantized tensor:", quantized_tensor)
print("Dequantized tensor:", dequantized_tensor)
