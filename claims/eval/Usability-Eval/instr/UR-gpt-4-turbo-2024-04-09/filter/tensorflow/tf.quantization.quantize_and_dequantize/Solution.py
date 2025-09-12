import tensorflow as tf

# Create a float tensor
float_tensor = tf.constant([[1.0, 2.0], [3.0, 4.0]], dtype=tf.float32)

# Apply quantization and dequantization
quantized_tensor, min_val, max_val = tf.quantization.quantize(float_tensor, min_range=0.0, max_range=4.0, T=tf.qint32, mode='MIN_COMBINED', round_mode='HALF_AWAY_FROM_ZERO')
dequantized_tensor = tf.quantization.dequantize(quantized_tensor, min_val, max_val, mode='MIN_COMBINED')

print("Original Tensor:")
print(float_tensor.numpy())
print("Quantized Tensor:")
print(quantized_tensor.numpy())
print("Dequantized Tensor:")
print(dequantized_tensor.numpy())
