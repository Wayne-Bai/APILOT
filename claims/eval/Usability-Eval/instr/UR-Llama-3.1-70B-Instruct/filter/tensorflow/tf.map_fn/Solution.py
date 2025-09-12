# Import necessary libraries
import tensorflow as tf

# Function to transform elements by applying a given function to each element unstacked on axis 0
def transform_elems(elems, fn):
    """
    Transforms elems by applying fn to each element unstacked on axis 0.

    Args:
        elems (Tensor): Input tensor.
        fn (callable): Function to apply to each element.

    Returns:
        Tensor: Transformed tensor.
    """
    # Unstack elements on axis 0
    unstacked_elems = tf.unstack(elems, axis=0)
    
    # Apply the function to each element
    transformed_elems = [fn(elem) for elem in unstacked_elems]
    
    # Stack the transformed elements back into a tensor
    transformed_tensor = tf.stack(transformed_elems, axis=0)
    
    return transformed_tensor

# Example usage:
# Define a simple function to square each element
def square_fn(x):
    return x ** 2

# Create a tensor
elems = tf.constant([1, 2, 3, 4, 5])

# Transform the tensor by applying the square function
transformed_tensor = transform_elems(elems, square_fn)

# Print the transformed tensor
print(transformed_tensor)
