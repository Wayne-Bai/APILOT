import tensorflow as tf

def quantized_elementwise_multiplication(x, y, x_min, x_max, y_min, y_max):
    # Adjust the input tensors based on their quantization parameters
    x = tf.quantization.quantize(x, x_min, x_max, tf.qint8)
    y = tf.quantization.quantize(y, y_min, y_max, tf.qint8)

    # Perform element-wise multiplication
    result = tf.multiply(x, y)

    # Dequantize the result back to float
    result_dequantized = tf.quantization.dequantize(result, x_min * y_min, x_max * y_max)

    return result_dequantized

# Example usage:
# Define example input tensors and quantization parameters
x = tf.constant([[1, 2], [3, 4]], dtype=tf.float32)
y = tf.constant([[5, 6], [7, 8]], dtype=tf.float32)
x_min = 0.0
x_max = 4.0
y_min = 0.0
y_max = 8.0

# Call the function
output = quantized_elementwise_multiplication(x, y, x_min, x_max, y_min, y_max)
print(output)
