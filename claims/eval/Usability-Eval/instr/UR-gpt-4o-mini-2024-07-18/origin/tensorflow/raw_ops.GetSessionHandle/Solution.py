import tensorflow as tf

@tf.function
def store_tensor(input_tensor):
    # Using tf.raw_ops to create a handle for the tensor
    tensor_handle = tf.raw_ops.StoreTensor(input_tensor=input_tensor)
    return tensor_handle

# Example usage
input_tensor = tf.constant([[1, 2], [3, 4]])
handle = store_tensor(input_tensor)

print("Tensor handle:", handle)
