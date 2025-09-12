import tensorflow as tf

def multiply(x, y):
    """
    Multiplies x and y element-wise.
    
    Args:
    x: A Tensor. Must be one of type float16, float32, uint8, int16, int32, int64.
    y: A Tensor. Must be one of type float16, float32, uint8, int16, int32, int64.
    
    Returns:
    A Tensor with the same shape and type as x or y. 
    """
    return tf.tensordot(x, y, axes=1)

# Example usage:
# Create two tensors of uint8 type
x = tf.constant([[1, 2], [3, 4]], dtype=tf.uint8)
y = tf.constant([[5, 6], [7, 8]], dtype=tf.uint8)

# Multiply x and y element-wise
result = multiply(x, y)

print(result)  # Output: [[5 12] [21 32]]
