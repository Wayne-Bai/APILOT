import tensorflow as tf

def create_ones_tensor(input_tensor):
    # Create a tensor of all ones with the same shape as the input tensor
    ones_tensor = tf.ones_like(input_tensor)
    return ones_tensor

# Example usage
input_tensor = tf.constant([[2, 3], [4, 5]])
ones_tensor = create_ones_tensor(input_tensor)

print(ones_tensor.numpy())
