import tensorflow as tf

# Define your Python function
def my_function(x):
    return x**2 + 1

# Wrap the function in a TensorFlow op
my_op = tf.py_func(my_function, [tf.constant(3.0)], tf.float64)

# Evaluate the op eagerly
result = my_op.numpy()

print(result)  # prints "10.0"
