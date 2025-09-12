import tensorflow as tf

def quantize_dequantize(tensor):
    # Get the min and max values for the tensor
    min_value = tf.reduce_min(tensor)
    max_value = tf.reduce_max(tensor)

    # Quantize the tensor using the min and max values
    quantized_tensor = tf.quantization.fake_quant_with_min_max_args(
        tensor, min=min_value, max=max_value, num_bits=8)

    # Dequantize the quantized tensor
    dequantized_tensor = tf.cast(quantized_tensor, dtype=tf.float32)

    return dequantized_tensor
