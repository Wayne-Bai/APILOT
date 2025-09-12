import tensorflow as tf

# Define a function to be applied to each element
def fn(x):
    # Your function implementation here
    return x * 2

# Assume you have a tensor with shape (10, 5)
tensor = tf.constant([[1, 2, 3, 4, 5],
                       [6, 7, 8, 9, 10],
                       # ... and so on
                       ])

# Apply the function to each element along axis 0
transformed_tensor = tf.map_fn(fn, tensor, dtype=tf.int32)

# Print the transformed tensor
print(transformed_tensor)
