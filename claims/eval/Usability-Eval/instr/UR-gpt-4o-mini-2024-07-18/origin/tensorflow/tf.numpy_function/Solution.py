import tensorflow as tf

# Define a simple Python function to wrap
def my_function(x):
    return x ** 2 + 2 * x + 1

# Create a TensorFlow operation using tf.py_function
@tf.function
def my_tf_op(x):
    return tf.py_function(func=my_function, inp=[x], Tout=tf.float32)

# Example usage
x = tf.constant([1.0, 2.0, 3.0])
result = my_tf_op(x)
print(result.numpy())
