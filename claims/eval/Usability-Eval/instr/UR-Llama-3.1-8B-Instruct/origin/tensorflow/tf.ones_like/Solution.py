import tensorflow as tf

def create_tensor_of_ones(input_tensor):
    return tf.ones_like(input_tensor)

# Example usage
input_tensor = tf.constant([[1, 2], [3, 4]])
print("Input Tensor:")
print(input_tensor)

tensor_of_ones = create_tensor_of_ones(input_tensor)
print("\nTensor of Ones:")
print(tensor_of_ones)
