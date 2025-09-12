import tensorflow as tf

def create_ones_tensor_like_input(input_tensor):
    return tf.ones_like(input_tensor)

# Example usage:
input_tensor = tf.constant([[2, 3], [4, 5], [6, 7]])
result_tensor = create_ones_tensor_like_input(input_tensor)
print(result_tensor)
