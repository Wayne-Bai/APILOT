
import tensorflow as tf

def dequantize_tensor(input_tensor):
    return tf.cast(input_tensor, tf.float32)

# Usage example
quantized_tensor = tf.constant([1, 2, 3], dtype=tf.uint8)
dequantized_tensor = dequantize_tensor(quantized_tensor)

print("Quantized Tensor:")
print(quantized_tensor)

print("\nDequantized Tensor:")
print(dequantized_tensor)
