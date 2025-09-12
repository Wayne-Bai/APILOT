# Importing the necessary library
import tensorflow as tf

# Function to create constant tensor
def create_constant_tensor(tensor_like_object):
    """
    Creates a constant tensor from a tensor-like object.
    
    Args:
        tensor_like_object (int, float, list, numpy.ndarray): 
            The input tensor-like object.

    Returns:
        tf.Tensor: A constant tensor created from the input tensor-like object.
    """
    # Create a constant tensor from the tensor-like object
    constant_tensor = tf.constant(tensor_like_object)

    return constant_tensor

# Example usage
# Create a constant tensor from a list
tensor_like_object = [1, 2, 3, 4, 5]
constant_tensor = create_constant_tensor(tensor_like_object)
print(constant_tensor)

# Create a constant tensor from a numpy array
import numpy as np
tensor_like_object = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
constant_tensor = create_constant_tensor(tensor_like_object)
print(constant_tensor)

# Create a constant tensor from an integer
tensor_like_object = 10
constant_tensor = create_constant_tensor(tensor_like_object)
print(constant_tensor)
