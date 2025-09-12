
import tensorflow as tf

# Create two datasets
dataset1 = tf.data.Dataset.range(1, 6) # Dataset with elements 1, 2, 3, 4, 5
dataset2 = tf.data.Dataset.range(6, 11) # Dataset with elements 6, 7, 8, 9, 10

# Zip the two datasets together
zipped_dataset = tf.data.Dataset.zip((dataset1, dataset2))

# Print the zipped dataset
for d1, d2 in zipped_dataset:
    print(d1.numpy(), d2.numpy())
