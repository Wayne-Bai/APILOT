import tensorflow as tf

def reverse_slices(input_tensor):
    # Reverse along the first dimension
    reversed_tensor = tf.reverse(input_tensor, axis=[0])
    return reversed_tensor

# Test the function
input_tensor = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
output_tensor = reverse_slices(input_tensor)
print(output_tensor.numpy())
