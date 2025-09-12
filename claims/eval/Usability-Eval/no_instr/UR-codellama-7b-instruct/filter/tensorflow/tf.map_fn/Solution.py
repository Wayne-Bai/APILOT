import tensorflow as tf

# Define the function to apply to each element in the tensor
def transform_fn(x):
    return x * 2 + 1

# Create a tensor with shape (3, 4) and values [1, 2, 3, 4, 5, 6, 7, 8, 9]
tensor = tf.convert_to_tensor([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Transform the tensor by applying the function to each element unstacked on axis 0
transformed_tensor = tf.map_fn(tf.nest.flatten, tensor)
