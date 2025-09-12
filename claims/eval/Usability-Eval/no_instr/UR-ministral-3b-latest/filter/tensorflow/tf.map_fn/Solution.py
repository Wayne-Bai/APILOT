import tensorflow as tf

# Define a sample transformation function (fn)
def transformation_function(x):
    return tf.matmul(x, tf.constant([[1, 2], [3, 4]]))

# Create a sample tensor
tensor = tf.constant([[1, 0], [2, 1], [3, -1]])

# Applying the transformation function to each element unstacked on axis 0.
transformed_tensors = tf.unstack(tf.map_fn(transformation_function, tensor, axis=0))

# Stack the unstacked tensors back together
transformed_tensor = tf.stack(transformed_tensors, axis=0)

print(transformed_tensor)
