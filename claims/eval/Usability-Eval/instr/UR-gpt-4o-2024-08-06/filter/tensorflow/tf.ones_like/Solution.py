import tensorflow as tf

# Function to create a tensor of all ones with the same shape as the input tensor
def create_ones_tensor(input_tensor):
    return tf.ones_like(input_tensor)

# Example usage
input_tensor = tf.constant([[1, 2, 3], [4, 5, 6]])
ones_tensor = create_ones_tensor(input_tensor)

print("Input Tensor:")
print(input_tensor.numpy())
print("Ones Tensor with the same shape:")
print(ones_tensor.numpy())
