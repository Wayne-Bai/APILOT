import tensorflow as tf

def multiply_quantized_buffers(x, y, min_x, max_x, min_y, max_y):
    # Quantize the first input
    x_quantized = tf.quantization.quantize(x, min_x, max_x, tf.quint8)
    
    # Quantize the second input
    y_quantized = tf.quantization.quantize(y, min_y, max_y, tf.quint8)
    
    # Multiply quantized tensors element-wise
    result = tf.raw_ops.QuantizedMul(
        x=x_quantized.output,
        y=y_quantized.output,
        min_x=x_quantized.output_min,
        max_x=x_quantized.output_max,
        min_y=y_quantized.output_min,
        max_y=y_quantized.output_max
    )
    
    # Dequantize the result to return it to float32
    result_dequantized = tf.quantization.dequantize(
        result.output,
        result.min_output,
        result.max_output
    )
    
    return result_dequantized
  
# Example usage
x = tf.constant([1.0, 2.5, 4.0], shape=[3], dtype=tf.float32)
y = tf.constant([2.0, 0.5, 3.0], shape=[3], dtype=tf.float32)

result = multiply_quantized_buffers(x, y, 0.0, 5.0, 0.0, 3.0)
print(result)
