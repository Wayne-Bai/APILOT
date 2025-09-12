import tensorflow as tf

def create_ones_tensor_like(input_tensor):
    return tf.ones_like(input_tensor)

# Example of usage:
input_tensor = tf.constant([[2, 3], [4, 5]])
output_tensor = create_ones_tensor_like(input_tensor)
print(output_tensor)
