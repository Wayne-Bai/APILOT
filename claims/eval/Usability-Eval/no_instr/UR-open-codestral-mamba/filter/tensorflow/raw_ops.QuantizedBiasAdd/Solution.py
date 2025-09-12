import tensorflow as tf

def add_bias(input, bias):
    return input + bias

# Usage
input_tensor = tf.constant([1, 2, 3], dtype=tf.int8)
bias_tensor = tf.constant([4, 5, 6], dtype=tf.int8)

result = add_bias(input_tensor, bias_tensor)
print(result)
