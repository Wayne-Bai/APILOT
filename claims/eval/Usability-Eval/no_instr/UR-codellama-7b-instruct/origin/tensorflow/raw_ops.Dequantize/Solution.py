
import tensorflow as tf

# Define the 'input' tensor
input_tensor = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0])

# Dequantize the 'input' tensor into a float Tensor
float_tensor = tf.raw_ops.Dequantize(
    input=input_tensor,
    axis=-1,
    dtype=tf.float32,
    name=None
)

# Dequantize the 'input' tensor into a bfloat16 Tensor
bfloat16_tensor = tf.raw_ops.Dequantize(
    input=input_tensor,
    axis=-1,
    dtype=tf.bfloat16,
    name=None
)
