import tensorflow as tf

def dequantize_tensor(input_tensor, min_range, max_range, mode="MIN_COMBINED", dtype=tf.float32):
    # Calculate the scale and zero point
    if mode == "MIN_COMBINED":
        input_type = input_tensor.dtype
        if input_type == tf.quint8:
            zero_point = 0
        elif input_type == tf.qint8:
            zero_point = -128
        else:
            raise ValueError("Unsupported input type for MIN_COMBINED mode")
        
        scale = (max_range - min_range) / (tf.cast(tf.reduce_max(input_tensor), dtype) - tf.cast(tf.reduce_min(input_tensor), dtype))
        output_tensor = tf.cast(input_tensor, dtype) * scale + min_range - zero_point * scale
    
    elif mode == "SCALED":
        input_type = input_tensor.dtype
        if input_type == tf.quint8:
            zero_point = 0
        elif input_type == tf.qint8:
            zero_point = -128
        else:
            raise ValueError("Unsupported input type for SCALED mode")
        
        scale = (max_range - min_range) / (tf.cast(tf.reduce_max(input_tensor), dtype) - tf.cast(tf.reduce_min(input_tensor), dtype))
        output_tensor = tf.cast(input_tensor, dtype) * scale + min_range - zero_point * scale
    
    else:
        raise ValueError("Unsupported mode")
    
    return output_tensor

# Example usage:
# input_tensor = tf.constant([1, 2, 3, 4], dtype=tf.qint8)
# min_range = -1.0
# max_range = 1.0
# dequantized_tensor = dequantize_tensor(input_tensor, min_range, max_range)
# print(dequantized_tensor)
