import tensorflow as tf

def transform_elements(elems, fn):
    # Unstack the tensor along the first axis
    elems_unstacked = tf.unstack(elems, axis=0)
    # Apply the function fn to each element
    transformed = [fn(elem) for elem in elems_unstacked]
    # Restack the list of transformed elements back into a tensor
    result = tf.stack(transformed, axis=0)
    return result

# Example usage:
elems = tf.constant([[1, 2], [3, 4], [5, 6]])
fn = lambda x: x * 2  # Example function to double each element
output = transform_elements(elems, fn)
print(output)
