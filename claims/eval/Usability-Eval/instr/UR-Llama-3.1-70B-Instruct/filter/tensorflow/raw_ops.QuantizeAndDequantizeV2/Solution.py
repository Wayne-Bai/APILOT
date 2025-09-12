import tensorflow as tf

def quantize_and_dequantize(tensor, min_range, max_range, narrow_range=False, num_bits=8, signed=True):
    """
    This function mimics the behavior of tf.raw_opsQuantizeAndDequantize. It quantizes a tensor and then dequantizes it.
    
    Args:
    tensor (tf.Tensor): The input tensor to be quantized and dequantized.
    min_range (float): The minimum value of the range.
    max_range (float): The maximum value of the range.
    narrow_range (bool): If True, then the quantized “range” is limited to [0, 2^num_bits - 1], otherwise [0, 2^num_bits].
    num_bits (int): The number of bits to use for quantization.
    signed (bool): If True, the quantized output will be signed, otherwise it will be unsigned.
    
    Returns:
    tf.Tensor: The dequantized tensor.
    """

    # Calculate the scale factor
    if narrow_range:
        range_size = 2**(num_bits - 1)
    else:
        range_size = 2**num_bits - 1
    
    if signed:
        quant_min = -range_size
        quant_max = range_size - 1
    else:
        quant_min = 0
        quant_max = range_size - 1
    
    scale_factor = (max_range - min_range) / (quant_max - quant_min)
    
    # Quantize the tensor
    tensor_quantized = tf.cast(tf.round((tensor - min_range) / scale_factor), tf.int32)
    
    # Clip the quantized tensor to the valid range
    tensor_clipped = tf.clip_by_value(tensor_quantized, quant_min, quant_max)
    
    # Dequantize the tensor
    tensor_dequantized = tf.cast(tensor_clipped, tf.float32) * scale_factor + min_range
    
    return tensor_dequantized

# Example usage:
tensor = tf.constant([1.2, 2.3, 3.4, 4.5], dtype=tf.float32)
min_range = 0.0
max_range = 10.0

dequantized_tensor = quantize_and_dequantize(tensor, min_range, max_range)
print(dequantized_tensor)
