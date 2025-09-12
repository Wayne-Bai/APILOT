import tensorflow as tf

def quantized_mul(x, y):
    # Ensure the inputs are quantized tensors
    if not (isinstance(x, tf.Tensor) and isinstance(y, tf.Tensor)):
        raise ValueError("Both inputs must be TensorFlow tensors.")
    
    # Perform element-wise multiplication
    result = tf.multiply(x, y)
    
    # If the inputs are quantized, the result will also be quantized
    return result

# Example usage:
# Assuming x and y are quantized tensors
x = tf.constant([1, 2, 3], dtype=tf.qint8)
y = tf.constant([4, 5, 6], dtype=tf.qint8)

# Perform quantized multiplication
result = quantized_mul(x, y)

# Print the result
print(result)
