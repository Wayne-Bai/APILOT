import tensorflow as tf

# Define a dataset of integers from 1 to 5
dataset = tf.data.Dataset.range(1, 6)

# Map a function that squares each element
squared_dataset = dataset.map(lambda x: x**2)

# Prefetch elements before usage
prefetched_dataset = squared_dataset.prefetch(tf.data.AUTOTUNE)

# Create an iterator from the prefetched dataset
iterator = tf.data.Iterator.from_structure(prefetched_dataset.output_types, prefetched_dataset.output_shapes)

# Set the iterator to start background threads of asynchronous transformations upon creation
iterator._set_background_threads(True)

# Get the next element from the iterator
next_element = iterator.get_next()

print(next_element)  # prints the square of 1, which is 1
