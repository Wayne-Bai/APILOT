import tensorflow as tf

# Create a sample tensor
tensor = tf.constant([[1.0, 2.0], [3.0, 4.0]], dtype=tf.float32)

# Quantize the tensor
# Here, we use tf.quantization.quantize to perform the quantization
# Note: This requires the tensor to be in the range of [0, 255] for uint8
min_val = tf.reduce_min(tensor)
max_val = tf.reduce_max(tensor)

quantized_tensor = tf.quantization.quantize(tensor, min_val, max_val, tf.dtypes.quantized.uint8, mode='MIN_COMBINED')

# Dequantize the tensor
dequantized_tensor = tf.quantization.dequantize(quantized_tensor[0], min_val, max_val)

print("Original Tensor:")
print(tensor.numpy())
print("\nQuantized Tensor:")
print(quantized_tensor[0].numpy())
print("\nDequantized Tensor:")
print(dequantized_tensor.numpy())
