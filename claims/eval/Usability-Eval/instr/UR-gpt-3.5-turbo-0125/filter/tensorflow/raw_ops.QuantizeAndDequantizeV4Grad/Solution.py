
import tensorflow as tf

@tf.custom_gradient
def custom_quantize_and_dequantize_v4(x):
    def gradient(dy):
        return dy

    return tf.quantize_and_dequantize_v2(x), gradient

# Example usage
input_tensor = tf.constant([1.5, 2.5, 3.5])
quantized_tensor = custom_quantize_and_dequantize_v4(input_tensor)

print(quantized_tensor)
