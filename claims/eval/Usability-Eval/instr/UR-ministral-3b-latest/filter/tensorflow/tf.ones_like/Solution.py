import tensorflow as tf

def create_tensor_of_ones(input_tensor):
    ones_tensor = tf.ones(input_tensor.shape)
    return ones_tensor

# Example usage
input_tensor = tf.constant([[1, 2, 3], [4, 5, 6]])
result_tensor = create_tensor_of_ones(input_tensor)
print(result_tensor)
