import tensorflow as tf

def quantized_elementwise_mul(x, y, min_x, max_x, min_y, max_y):
    # Convert inputs to tensors if they are not already.
    x = tf.convert_to_tensor(x, dtype=tf.float32)
    y = tf.convert_to_tensor(y, dtype=tf.float32)
    
    # Quantization parameters
    min_x = tf.convert_to_tensor(min_x, dtype=tf.float32)
    max_x = tf.convert_to_tensor(max_x, dtype=tf.float32)
    min_y = tf.convert_to_tensor(min_y, dtype=tf.float32)
    max_y = tf.convert_to_tensor(max_y, dtype=tf.float32)
    
    # Simulating quantization by normalizing values to [0, 255]
    # and then scaling to [min, max] for the purpose of calculation
    x_normalized = tf.quantization.quantize(x, min_x, max_x, tf.quint8)
    y_normalized = tf.quantization.quantize(y, min_y, max_y, tf.quint8)
    
    # Since tf.raw_ops.QuantizedMul is outdated and should not be used, we convert back to float
    x_dequantized = tf.quantization.dequantize(
        x_normalized.output, x_normalized.output_min, x_normalized.output_max,
        dtype=tf.float32
    )
    y_dequantized = tf.quantization.dequantize(
        y_normalized.output, y_normalized.output_min, y_normalized.output_max,
        dtype=tf.float32
    )
    
    # Element-wise multiplication
    result = tf.multiply(x_dequantized, y_dequantized)
    
    return result
