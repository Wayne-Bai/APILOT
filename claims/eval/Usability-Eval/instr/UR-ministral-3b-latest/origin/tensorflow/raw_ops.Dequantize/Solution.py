import tensorflow as tf

# Assuming `input_tensor` is the desired input tensor.
input_tensor = tf.constant([0.1, 0.2, 0.3, 0.4], dtype=tf.float32)

# Dequantize the input tensor.
dequantized_tensor = tf.cast(input_tensor, tf.float32)  # If you need float32
# dequantized_tensor = tf.cast(input_tensor, tf.bfloat16)  # If you need bfloat16

print(dequantized_tensor)
