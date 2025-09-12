
import tensorflow as tf

# Define the function that will be applied to each element of the input tensor
def my_fn(x):
    return x + 1

# Create a dataset from a list of input values
inputs = [[1, 2], [3, 4], [5, 6]]
dataset = tf.data.Dataset.from_tensor_slices(inputs)

# Map the function on each element of the dataset unstacked on axis 0
outputs = dataset.map(lambda x: tf.map_fn(my_fn, x, dtype=tf.float32))
