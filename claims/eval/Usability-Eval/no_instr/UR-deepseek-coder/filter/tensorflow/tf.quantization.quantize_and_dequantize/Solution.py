import tensorflow as tf

def quantize_and_dequantize(tensor, num_bits=8, signed=True, range_given=False, input_min=0.0, input_max=1.0):
    # Quantize the tensor
    if range_given:
        scale = (input_max - input_min) / (2 ** num_bits - 1)
        quantized_tensor = tf.round((tensor - input_min) / scale)
    else:
        min_value = tf.reduce_min(tensor)
        max_value = tf.reduce_max(tensor)
        scale = (max_value - min_value) / (2 ** num_bits - 1)
        quantized_tensor = tf.round((tensor - min_value) / scale)

    # Dequantize the tensor
    dequantized_tensor = quantized_tensor * scale + (input_min if range_given else min_value)

    return dequantized_tensor

# Example usage
tensor = tf.constant([0.1, 0.5, 0.9])
dequantized_tensor = quantize_and_dequantize(tensor, num_bits=8, signed=False, range_given=True, input_min=0.0, input_max=1.0)

print(dequantized_tensor.numpy())
