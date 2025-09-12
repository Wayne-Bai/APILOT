import tensorflow as tf

# Define a Python function
def add_scalar(x, scalar):
    return x + scalar

# Register Python function as TensorFlow op
add_scalar_op = tf.py_function(add_scalar, inp=[tf.float32, tf.float32], Tout=tf.float32)

# Use the new op
with tf.Session() as sess:
    print(sess.run(add_scalar_op([1, 2, 3], 10)))
