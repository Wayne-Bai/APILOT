import tensorflow as tf

# Assume fn is a function that transforms elements
def transform_fn(x):
    return tf.square(x)

# Assume input tensor is a tensor with shape (batch_size, sequence_length)
input_tensor = tf.random.normal([32, 10])

# Unstack the tensor on axis 0 and apply the transformation function
transformed_tensor = tf.unstack(input_tensor, axis=0, out_type=tf.float32)
transformed_tensor = [transform_fn(elem) for elem in transformed_tensor]
transformed_tensor = tf.stack(transformed_tensor, axis=0)
