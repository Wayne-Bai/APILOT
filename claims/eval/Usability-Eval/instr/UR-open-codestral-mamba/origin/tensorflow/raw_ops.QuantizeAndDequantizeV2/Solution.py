import tensorflow as tf

# Create an input tensor
input_tensor = tf.constant([-1.2, 0.3, 2.5, -0.6], dtype=tf.float32)

# Quantization parameters
min_range = -2.0
max_range = 2.0

# Quantize the tensor
q_tensor = tf.raw_ops.QuantizeAndDequantize(
    input=input_tensor,
    Tinput=tf.float32,
    Toutput=tf.float32,
    min_range=min_range,
    max_range=max_range
)

print(q_tensor)
