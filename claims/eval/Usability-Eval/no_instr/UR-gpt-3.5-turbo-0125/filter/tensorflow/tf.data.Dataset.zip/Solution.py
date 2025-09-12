
import tensorflow as tf

# Define input datasets
dataset1 = tf.data.Dataset.from_tensor_slices([1, 2, 3])
dataset2 = tf.data.Dataset.from_tensor_slices(['a', 'b', 'c'])

# Zip together the datasets
zipped_dataset = tf.data.Dataset.zip((dataset1, dataset2))

# Iterate through the zipped dataset to confirm the zipping
for data in zipped_dataset:
    print(data)
