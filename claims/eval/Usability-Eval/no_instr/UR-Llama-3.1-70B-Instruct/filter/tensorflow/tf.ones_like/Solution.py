# Import the necessary libraries
import tensorflow as tf

# Function to create a tensor of ones with the same shape as the input
def create_ones_tensor(input_tensor):
    # Use tf.ones_like to create a tensor of ones with the same shape as the input
    ones_tensor = tf.ones_like(input_tensor)
    return ones_tensor

# Create a sample input tensor
input_tensor = tf.constant([[1, 2, 3], [4, 5, 6]])

# Create a tensor of ones with the same shape as the input
ones_tensor = create_ones_tensor(input_tensor)

print("Input Tensor:")
print(input_tensor)
print("\nTensor of Ones with Same Shape:")
print(ones_tensor)
