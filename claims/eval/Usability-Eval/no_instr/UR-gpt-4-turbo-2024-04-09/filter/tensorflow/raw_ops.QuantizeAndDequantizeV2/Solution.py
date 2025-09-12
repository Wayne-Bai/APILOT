import tensorflow as tf

def quantize_then_dequantize(tensor, min_range, max_range):
    # Quantizing tensor
    quantized_tensor = tf.quantization.quantize(
        input=tensor,
        min_range=min_range,
        max_range=max_range,
        T=tf.qint8,
        mode='MIN_COMBINED',
        round_mode='HALF_AWAY_FROM_ZERO'
    )
    
    # Dequantizing tensor
    dequantized_tensor = tf.quantization.dequantize(
        input=quantized_tensor.output,
        min_range=min_range,
        max_range=max_range,
        mode='MIN_COMBINED'
    )
    
    return dequantized_tensor

# Example tensor
example_tensor = tf.constant([1.2, 3.4, -1.0, 4.5], dtype=tf.float32)

# Minimum and maximum range for quantization
min_val = tf.reduce_min(example_tensor)
max_val = tf.reduce_max(example_tensor)

dequantized_output = quantize_then_dequantize(example_tensor, min_val, max_val)
print(dequantized_output)
