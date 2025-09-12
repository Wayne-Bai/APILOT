import tensorflow as tf

# Create two datasets
dataset1 = tf.data.Dataset.range(10)
dataset2 = tf.data.Dataset.from_tensor_slices([1, 2, 3])

# Zip the two datasets together
zipped_dataset = dataset1.zip(dataset2)
