
import tensorflow as tf

# Define a custom function using tf.py_function
@tf.function
def my_func(x):
    return x + 1

# Create a tensor using tf.constant
tensor = tf.constant([1, 2, 3])

# Apply the custom function to the tensor
result = my_func(tensor)

print(result)
