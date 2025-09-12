import tensorflow as tf

@tf.function
def custom_op_function(x):
    return x * 2 + 1

# Example of using the function within a TensorFlow session
x = tf.constant([1, 2, 3])
result = custom_op_function(x)
print(result)
