import tensorflow as tf

# Define the datasets
dataset1 = tf.data.Dataset.from_tensor_slices([1, 2, 3])
dataset2 = tf.data.Dataset.from_tensor_slices(['a', 'b', 'c'])

# Zip the datasets
zipped_dataset = tf.data.Dataset.zip((dataset1, dataset2))

# Iterate over the zipped dataset
for element in zipped_dataset:
    print(element)
