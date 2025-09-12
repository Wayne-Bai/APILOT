import tensorflow as tf

# Example tensor
tensor = tf.constant([[1, 2, 3], [4, 5, 6]])

# Function to apply to each element
def transform_fn(x):
    return x * 2

# Unstack along axis 0 and transform each element
transformed_elems = [transform_fn(elem) for elem in tf.unstack(tensor, axis=0)]

# Combine the results back into a tensor
result_tensor = tf.stack(transformed_elems, axis=0)

print(result_tensor)
