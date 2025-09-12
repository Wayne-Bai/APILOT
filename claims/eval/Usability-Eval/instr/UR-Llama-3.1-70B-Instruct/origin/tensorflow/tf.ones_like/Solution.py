# Import the necessary library
import tensorflow as tf

# Function to create a tensor of all ones with the same shape as the input
def create_ones_tensor(input_tensor):
    """
    Creates a tensor of all ones that has the same shape as the input tensor.

    Args:
        input_tensor (tf.Tensor): The input tensor.

    Returns:
        tf.Tensor: A tensor of all ones with the same shape as the input tensor.
    """
    return tf.ones_like(input_tensor)

# Example usage
input_tensor = tf.constant([1, 2, 3, 4, 5], shape=(1, 5))
ones_tensor = create_ones_tensor(input_tensor)

print("Input Tensor: ", input_tensor)
print("Ones Tensor: ", ones_tensor)
