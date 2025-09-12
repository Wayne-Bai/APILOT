import tensorflow as tf

def quantized_elementwise_multiply(x, y):
    # Ensure that x and y are quantized tensors
    if not (tf.experimental.numpy.issubdtype(x.dtype, tf.int) and tf.experimental.numpy.issubdtype(y.dtype, tf.int)):
        raise ValueError("Both x and y must be quantized tensors.")

    # Use tf.multiply for element-wise multiplication
    result = tf.multiply(x, y)

    return result

# Example usage
x = tf.constant([1, 2, 3], dtype=tf.int32)  # A quantized tensor
y = tf.constant([4, 5, 6], dtype=tf.int32)  # Another quantized tensor

result = quantized_elementwise_multiply(x, y)
print(result)
