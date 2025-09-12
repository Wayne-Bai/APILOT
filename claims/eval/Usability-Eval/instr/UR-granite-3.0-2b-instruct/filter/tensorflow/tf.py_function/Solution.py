import tensorflow as tf

# Define your Python function
def my_function(x):
    return tf.square(x)

# Wrap the function into a TensorFlow op
my_op = tf.function(my_function)

# Execute the op eagerly
result = my_op(2.0)

print(result)
