import tensorflow as tf

# Create a TensorFlow session
@tf.function
def store_tensor_value(input_tensor):
    # Use tf.raw_ops.define to store the input tensor in the session
    handle = tf.raw_ops.CreateVariable(
        container="",
        shared_name="my_tensor_handle",
        dtype=input_tensor.dtype,
        shape=input_tensor.shape,
        use_resource=True,
        initial_value=input_tensor
    )
    return handle

# Example usage
input_tensor = tf.constant([[1, 2], [3, 4]])
tensor_handle = store_tensor_value(input_tensor)

# To retrieve the value stored in the handle in a different part of your program, 
# you would typically need to perform further operations.
# Note: Actual retrieval is not shown as it requires operations generally used in a session.
