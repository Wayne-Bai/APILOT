import tensorflow as tf

def create_ones_tensor(input_tensor):
    return tf.ones_like(input_tensor)

# Example usage:
# input_tensor = tf.constant([[1, 2], [3, 4]])
# ones_tensor = create_ones_tensor(input_tensor)
# print(ones_tensor)
