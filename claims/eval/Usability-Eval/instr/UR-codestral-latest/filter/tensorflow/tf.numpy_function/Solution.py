import tensorflow as tf

def my_python_function(x, y):
    return tf.math.add(x, y)

@tf.function
def my_tf_function(x, y):
    result = tf.py_function(my_python_function, [x, y], tf.float32)
    return result

# Test the function
x = tf.constant([1, 2, 3], dtype=tf.float32)
y = tf.constant([4, 5, 6], dtype=tf.float32)
print(my_tf_function(x, y).numpy())
