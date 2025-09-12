import tensorflow as tf

# Create example datasets
dataset1 = tf.data.Dataset.from_tensor_slices([1, 2, 3, 4])
dataset2 = tf.data.Dataset.from_tensor_slices(['a', 'b', 'c', 'd'])

# Zip the datasets together
zipped_dataset = tf.data.Dataset.zip((dataset1, dataset2))

# Iterate over the zipped dataset and print the results
for element in zipped_dataset:
    print(element)
