
import tensorflow as tf

# Create a nested list
my_list = [[1, 2], [3, 4]]

# Flatten the nested list using tf.nest.flatten
flattened_list = tf.nest.flatten(my_list)
print(flattened_list)  # prints [1, 2, 3, 4]

# Map a function to the flattened list
def square(x):
    return x ** 2

squared_list = tf.nest.map_fn(square, flattened_list)
print(squared_list)  # prints [1, 4, 9, 16]
