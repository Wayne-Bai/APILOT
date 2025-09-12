import tensorflow as tf

# Define a function to reverse variable length slices
def reverse_slices(input_tensor):
    # Create a new tensor with the same shape as the input tensor
    reversed_tensor = tf.reverse(input_tensor, [0])
    return reversed_tensor

# Create a sample input tensor
input_tensor = tf.constant([[1, 2, 3], [4, 5], [6, 7, 8, 9]])

# Call the function to reverse the variable length slices
reversed_tensor = reverse_slices(input_tensor)

# Print the original and reversed tensors
print("Original Tensor:")
print(input_tensor)
print("\nReversed Tensor:")
print(reversed_tensor)
