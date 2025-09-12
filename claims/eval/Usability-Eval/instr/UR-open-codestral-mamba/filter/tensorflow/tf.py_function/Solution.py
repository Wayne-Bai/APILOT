import tensorflow as tf

# Assuming we have the following simple function
def add_two(x):
    return x + 2

# We can convert it into a TensorFlow op using tf.py_function
add_two_tf = tf.py_function(add_two, inp=[tf.constant(3)], Tout=tf.int32)

# execute the operation directly in eager mode
result = add_two_tf.numpy()
result
