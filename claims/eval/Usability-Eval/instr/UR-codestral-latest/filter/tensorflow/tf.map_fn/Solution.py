import tensorflow as tf

def apply_function_to_each_element(tensor, fn):
    """
    Transforms elements by applying fn to each element unstacked on axis 0.
    """
    # Unstack the tensor along axis 0
    unstacked_tensor = tf.unstack(tensor, axis=0)

    # Apply the function to each element
    transformed_elements = [fn(elem) for elem in unstacked_tensor]

    # Stack the transformed elements back together along axis 0
    transformed_tensor = tf.stack(transformed_elements, axis=0)

    return transformed_tensor

# Example usage:
tensor = tf.constant([[1, 2, 3], [4, 5, 6]])
fn = tf.square  # Replace this with your actual function
result = apply_function_to_each_element(tensor, fn)
