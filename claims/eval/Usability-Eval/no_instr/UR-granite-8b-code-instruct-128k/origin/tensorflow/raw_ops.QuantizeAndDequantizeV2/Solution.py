import tensorflow as tf

# Create a tensor to quantize and dequantize
x = tf.constant([[1.2, 2.3, 3.4], [-4.5, -5.6, -6.7]])

# Quantize the tensor to 8 bits
y, min_val, max_val = tf.raw_ops.QuantizeAndDequantizeV2(
    input=x, min_range=0.0, max_range=10.0, T=tf.quint8)

# Dequantize the tensor
z = tf.raw_ops.QuantizeAndDequantizeV2(
    input=y, min_range=min_val, max_range=max_val, T=tf.float32)

# Print the quantized and dequantized tensors
print("Quantized tensor:", y.numpy())
print("Dequantized tensor:", z.numpy())
