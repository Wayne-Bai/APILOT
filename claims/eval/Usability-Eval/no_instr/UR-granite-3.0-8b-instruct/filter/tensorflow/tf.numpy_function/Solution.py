import tensorflow as tf

# Define a Python function
def my_python_function(x):
    return x * 2

# Wrap the Python function as a TensorFlow op
my_tf_op = tf.py_function(my_python_function, inp=[tf.constant([1, 2, 3])], Tout=tf.int32)

# Run the TensorFlow op
with tf.Session() as sess:
    result = sess.run(my_tf_op)
    print(result)
