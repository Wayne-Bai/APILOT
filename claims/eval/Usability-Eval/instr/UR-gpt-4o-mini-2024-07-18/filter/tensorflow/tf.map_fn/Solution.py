import tensorflow as tf

def transform_elems(tensor, fn):
    # Unstack tensor along axis 0
    unstacked_tensors = tf.unstack(tensor, axis=0)
    # Apply fn to each unstacked element
    transformed_tensors = [fn(elem) for elem in unstacked_tensors]
    # Stack back the transformed tensors along axis 0
    return tf.stack(transformed_tensors)

# Example usage
input_tensor = tf.constant([[1, 2], [3, 4], [5, 6]])
output_tensor = transform_elems(input_tensor, lambda x: x + 10)
print(output_tensor)
