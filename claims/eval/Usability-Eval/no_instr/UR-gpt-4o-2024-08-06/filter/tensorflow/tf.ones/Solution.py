import tensorflow as tf

# Create a tensor with all elements set to one
def create_ones_tensor(shape, dtype=tf.float32):
    return tf.ones(shape, dtype=dtype)

# Example usage
tensor_shape = (3, 4)  # Shape of the tensor
ones_tensor = create_ones_tensor(tensor_shape)
print(ones_tensor)
