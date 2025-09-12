import tensorflow as tf

def transpose_tensor(a):
    return tf.transpose(a)

# Example usage
a = tf.constant([[1, 2, 3], [4, 5, 6]])
transposed_a = transpose_tensor(a)
print(transposed_a)
