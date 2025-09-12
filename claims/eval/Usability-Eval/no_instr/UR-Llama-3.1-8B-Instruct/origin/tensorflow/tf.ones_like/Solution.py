import tensorflow as tf

def create_tensor_of_ones(input_tensor):
    """
    Creates a tensor of all ones that has the same shape as the input.

    Args:
    input_tensor (tf.Tensor): The input tensor.

    Returns:
    tf.Tensor: A tensor of all ones with the same shape as the input.
    """
    # Use tf.ones to create a tensor of all ones with the same shape as the input
    tensor_of_ones = tf.ones_like(input_tensor)
    
    return tensor_of_ones

# Example usage:
input_tensor = tf.random.normal((3, 3))
print("Input Tensor:")
print(input_tensor)

tensor_of_ones = create_tensor_of_ones(input_tensor)
print("\nTensor of Ones:")
print(tensor_of_ones)
