# Import the required libraries
import tensorflow as tf

# Define a function to transpose a tensor
def transpose_tensor(a):
    """
    Transposes the input tensor.

    Args:
        a (tf.Tensor): The input tensor to be transposed.

    Returns:
        tf.Tensor: The transposed tensor.
    """
    return tf.transpose(a)

# Create a sample tensor
tensor_a = tf.constant([[1, 2], [3, 4]])

# Transpose the tensor
transposed_tensor = transpose_tensor(tensor_a)

# Print the transposed tensor
print(transposed_tensor)

# Expected output:
# tf.Tensor(
# [[1 3]
#  [2 4]], shape=(2, 2), dtype=int32)
