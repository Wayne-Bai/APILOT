import tensorflow as tf

def multiply_quantized_buffers(x, y):
    # Convert the input buffers to tf.int32
    x_int32 = tf.cast(x, tf.int32)
    y_int32 = tf.cast(y, tf.int32)

    # Multiply the buffers element-wise using tf.raw_ops
    result = tf.raw_ops.Mul(x=x_int32, y=y_int32)

    return result

# Example usage
if __name__ == "__main__":
    # Initialize the quantized buffers
    x = tf.constant([1, 2, 3, 4], dtype=tf.uint8)
    y = tf.constant([5, 6, 7, 8], dtype=tf.uint8)

    # Multiply the quantized buffers
    result = multiply_quantized_buffers(x, y)

    # Print the result
    print("Result of multiplying quantized buffers:", result)
