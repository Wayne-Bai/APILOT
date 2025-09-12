import tensorflow as tf

# Assume we have two datasets, which are lists of numbers
dataset1 = tf.data.Dataset.from_tensor_slices([1, 2, 3, 4, 5])
dataset2 = tf.data.Dataset.from_tensor_slices(['a', 'b', 'c', 'd', 'e'])

# We can zip these two datasets together using the zip method
zipped_dataset = tf.data.Dataset.zip((dataset1, dataset2))

# Now, zipped_dataset is a dataset of tuples, where each tuple contains one element from each of the original datasets
for item in zipped_dataset:
    print(item)
