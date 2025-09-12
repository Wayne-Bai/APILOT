# Import the necessary library
import tensorflow as tf

# Create a tensor filled with a scalar value
def create_filled_tensor(shape, scalar_value):
    """
    Creates a tensor of specified shape filled with a scalar value.

    Args:
        shape (list or tuple): The shape of the tensor to be created.
        scalar_value (int or float): The scalar value to fill the tensor with.

    Returns:
        tf.Tensor: A tensor of specified shape filled with the scalar value.
    """
    # Use tf.fill to create a tensor filled with the scalar value
    filled_tensor = tf.fill(dims=shape, value=scalar_value)
    return filled_tensor

# Test the function
shape = [2, 3]
scalar_value = 5
filled_tensor = create_filled_tensor(shape, scalar_value)
print(filled_tensor)
