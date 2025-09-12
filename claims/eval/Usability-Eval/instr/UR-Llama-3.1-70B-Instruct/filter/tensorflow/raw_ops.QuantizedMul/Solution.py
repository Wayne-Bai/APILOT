import tensorflow as tf

def quantized_multiply(x, y, x_min, x_max, y_min, y_max, T):
    """
    This function mimics the behavior of QuantizedMul in TensorFlow, 
    which has been deprecated in recent versions. 

    It takes in two tensors, x and y, along with their respective 
    minimum and maximum quantization values, and the desired type.

    Args:
    x (tf.Tensor): First tensor
    y (tf.Tensor): Second tensor
    x_min (tf.Tensor): Minimum quantization value of x
    x_max (tf.Tensor): Maximum quantization value of x
    y_min (tf.Tensor): Minimum quantization value of y
    y_max (tf.Tensor): Maximum quantization value of y
    T (tf.dtype): Desired type

    Returns:
    tf.Tensor: x * y element-wise
    """

    # Create fallback multiplier
    def fallback(op, x, y):
        cast_x = tf.cast(x, tf.float32)
        cast_y = tf.cast(y, tf.float32)
        return tf.cast(tf.math.multiply(cast_x, cast_y), T)

    # Register fallback
    tf.register_tensor_conversion_function(fallback, fallback_priority=-1)

    # Use multiply
    result = tf.math.multiply(x, y)

    # Clip results according to x_min, x_max, y_min, y_max
    result = tf.clip_by_value(result, tf.reduce_min([x_min * y_min, x_min * y_max, x_max * y_min, x_max * y_max]), 
                              tf.reduce_max([x_min * y_min, x_min * y_max, x_max * y_min, x_max * y_max]))

    return result

# Example usage
x = tf.constant([1, 2, 3, 4], dtype=tf.uint8)
y = tf.constant([4, 5, 6, 7], dtype=tf.uint8)

x_min = tf.constant(0, dtype=tf.uint8)
x_max = tf.constant(255, dtype=tf.uint8)
y_min = tf.constant(0, dtype=tf.uint8)
y_max = tf.constant(255, dtype=tf.uint8)

result = quantized_multiply(x, y, x_min, x_max, y_min, y_max, tf.uint8)
print(result)
