import tensorflow as tf

def quantized_multiply(x, y):
    # Assuming x and y are quantized tensors
    x_quantized = tf.quantization.quantize(x, min_range=0.0, max_range=1.0, T=tf.quint8)
    y_quantized = tf.quantization.quantize(y, min_range=0.0, max_range=1.0, T=tf.quint8)
    
    # Perform element-wise multiplication on quantized tensors
    product_quantized = tf.quantization.dequantize(x_quantized[0] * y_quantized[0], x_quantized[1], x_quantized[2])
    
    return product_quantized

# Example usage
x = tf.constant([1.0, 2.0, 3.0])
y = tf.constant([4.0, 5.0, 6.0])
result = quantized_multiply(x, y)
print(result.numpy())
