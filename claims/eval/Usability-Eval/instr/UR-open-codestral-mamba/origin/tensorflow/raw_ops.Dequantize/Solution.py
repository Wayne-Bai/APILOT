import tensorflow as tf

def dequantize(input, input_min, input_max):
    # Check if input is a bfloat16 Tensor
    if input.dtype == tf.bfloat16:
        return tf.dtypes.cast(input, tf.float32)

    # Create a range of quantized values
    quantized_values = tf.range(tf.cast(input_min, tf.int32), tf.cast(input_max, tf.int32) + 1, dtype=tf.int32)

    # Convert input to float32 and subtract input_min
    dequantized_values = tf.dtypes.cast(input, tf.float32) - tf.dtypes.cast(input_min, tf.float32)

    # Calculate the quantization step
    quantization_step = (tf.dtypes.cast(input_max, tf.float32) - tf.dtypes.cast(input_min, tf.float32)) / tf.dtypes.cast(tf.size(quantized_values, out_type=tf.float32) - 1, tf.float32)

    # Dequantize the input tensor
    dequantized_tensor = quantization_step * tf.dtypes.cast(quantized_values, tf.float32) + tf.dtypes.cast(input_min, tf.float32)

    return dequantized_tensor

# Test the dequantize function
input_tensor = tf.constant([10, 20, 30], dtype=tf.int32)
input_min = 0
input_max = 255
output_tensor = dequantize(input_tensor, input_min, input_max)
print(output_tensor)
