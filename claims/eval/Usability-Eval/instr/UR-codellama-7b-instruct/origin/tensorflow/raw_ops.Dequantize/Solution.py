import tensorflow as tf

# Input tensor
x = tf.constant(2**8-1)

# Dequantize the input tensor into a float or bfloat16 Tensor
y = tf.raw_ops.DequantizeV2(input=x, signed_input=True)

print(y)

# Output: tf.Tensor([3.90625], shape=(1,), dtype=float32)