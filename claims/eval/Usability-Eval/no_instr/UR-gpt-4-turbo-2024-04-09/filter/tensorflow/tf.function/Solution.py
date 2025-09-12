import tensorflow as tf

@tf.function
def my_function(x):
    return x ** 2 + 5

# Example use:
x_input = tf.constant([2, 3, 4], dtype=tf.float32)
result = my_function(x_input)
print(result)
