import tensorflow as tf

# Define the function
@tf.function
def my_function(x):
    return tf.sin(x)

# Print the function
print(my_function)
