
import tensorflow as tf

# Create two random datasets
dataset1 = tf.data.Dataset.from_tensor_slices([[1, 2], [3, 4]])
dataset2 = tf.data.Dataset.from_tensor_slices([['a', 'b'], ['c', 'd']])

# Zip the two datasets together
zipped_dataset = dataset1.zip(dataset2)

# Create a new Dataset object by applying the map function
new_dataset = zipped_dataset.map(lambda x, y: (x[0] + y[0], x[1] + y[1]))
