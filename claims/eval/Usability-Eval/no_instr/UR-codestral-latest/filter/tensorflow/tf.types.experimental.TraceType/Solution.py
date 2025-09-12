import tensorflow as tf

@tf.function(input_signature=[tf.TensorSpec(shape=None, dtype=tf.float32),
                              tf.TensorSpec(shape=None, dtype=tf.float32)])
def my_function(x, y):
    return tf.multiply(x, y)

# Test the function
x = tf.constant(2.0, dtype=tf.float32)
y = tf.constant(3.0, dtype=tf.float32)
print(my_function(x, y))
