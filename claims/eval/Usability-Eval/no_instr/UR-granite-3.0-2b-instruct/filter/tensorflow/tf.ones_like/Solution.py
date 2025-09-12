import tensorflow as tf

# Create a tensor of all ones with the same shape as the input
def create_ones_tensor(input_tensor):
    ones_tensor = tf.ones_like(input_tensor)
    return ones_tensor

# Example usage
input_tensor = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
ones_tensor = create_ones_tensor(input_tensor)

print("Input Tensor:")
print(input_tensor)
print("\nOnes Tensor:")
print(ones_tensor)
