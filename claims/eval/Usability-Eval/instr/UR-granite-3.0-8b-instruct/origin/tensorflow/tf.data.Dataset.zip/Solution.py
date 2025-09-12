import tensorflow as tf

# Assuming you have two datasets, dataset1 and dataset2
dataset1 = ...
dataset2 = ...

# Create a zip dataset
zip_dataset = tf.data.Dataset.zip((dataset1, dataset2))
