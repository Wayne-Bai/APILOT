import tensorflow as tf

@tf.function
def my_function(x):
    # Your TensorFlow operations here
    y = tf.matmul(x, x)
    return y

# Test the function
result = my_function(tf.constant([[1, 2], [3, 4]]))
print(result)
