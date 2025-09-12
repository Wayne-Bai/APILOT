import tensorflow as tf

# Create example datasets
dataset1 = tf.data.Dataset.range(5)  # Dataset: 0, 1, 2, 3, 4
dataset2 = tf.data.Dataset.range(5, 10)  # Dataset: 5, 6, 7, 8, 9

# Zip the datasets together
zipped_dataset = tf.data.Dataset.zip((dataset1, dataset2))

# To verify output, let's iterate through the zipped dataset and print elements
for element in zipped_dataset:
    print(element)
