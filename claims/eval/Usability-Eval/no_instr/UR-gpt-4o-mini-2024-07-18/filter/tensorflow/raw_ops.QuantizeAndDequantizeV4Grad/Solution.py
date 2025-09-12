import tensorflow as tf

@tf.custom_gradient
def quantize_dequantize_gradients(input_tensor, min_val, max_val):
    def grad(dy):
        # The gradient simply passes through the input tensor.
        return dy, None, None
    
    # Quantize the input tensor
    quantized_tensor = tf.quantization.quantize(input_tensor, min_val, max_val, tf.qint32, tf.quantization.QuantizationMode.MIN_FIRST)[0]
    # Dequantize the tensor
    dequantized_tensor = tf.quantization.dequantize(quantized_tensor, min_val, max_val)
    
    return dequantized_tensor, grad

# Example usage
input_tensor = tf.constant([1.0, 2.0, 3.0], dtype=tf.float32)
min_val = tf.constant(0.0, dtype=tf.float32)
max_val = tf.constant(3.0, dtype=tf.float32)

result = quantize_dequantize_gradients(input_tensor, min_val, max_val)
print(result)
