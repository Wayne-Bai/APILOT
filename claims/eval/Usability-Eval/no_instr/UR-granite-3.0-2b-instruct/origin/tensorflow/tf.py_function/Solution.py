import tensorflow as tf

# Define your Python function
def my_function(x):
    return tf.square(x)

# Wrap the function into a TensorFlow operation
my_op = tf.function(my_function)

# Execute the operation eagerly
result = my_op(3.0)

print(result)
