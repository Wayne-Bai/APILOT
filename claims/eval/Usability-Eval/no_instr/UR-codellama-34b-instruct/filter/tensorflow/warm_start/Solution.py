import tensorflow as tf

# Define the dataset
dataset = tf.data.Dataset.from_tensor_slices([[1, 2], [3, 4]])

# Define the transformation function
def transform(x):
    return x * 2

# Apply the transformation in a background thread
dataset = dataset.map(transform)

# Prefetch data to improve latency
dataset = dataset.prefetch(10)

# Create an iterator from the dataset
iterator = dataset.make_one_shot_iterator()

# Get the next element from the iterator
next_element = iterator.get_next()
