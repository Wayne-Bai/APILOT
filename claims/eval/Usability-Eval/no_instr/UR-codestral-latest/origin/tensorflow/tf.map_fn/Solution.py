import tensorflow as tf

def apply_function_to_tensor(tensor, fn):
    # Unstack tensor along axis 0
    unstacked_tensor = tf.unstack(tensor, axis=0)

    # Apply function to each element
    transformed_elements = [fn(element) for element in unstacked_tensor]

    # Stack transformed elements back together
    transformed_tensor = tf.stack(transformed_elements, axis=0)

    return transformed_tensor

# Define your function here, for example a simple addition
def fn(x):
    return x + 1

# Define your tensor here
tensor = tf.constant([[1, 2, 3], [4, 5, 6]])

# Apply function to tensor
transformed_tensor = apply_function_to_tensor(tensor, fn)
