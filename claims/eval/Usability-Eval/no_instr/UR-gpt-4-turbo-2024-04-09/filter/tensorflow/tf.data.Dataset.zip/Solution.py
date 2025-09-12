import tensorflow as tf

# Create example datasets
dataset1 = tf.data.Dataset.range(5)
dataset2 = tf.data.Dataset.range(5, 10)

# Zip the datasets together
zipped_dataset = tf.data.Dataset.zip((dataset1, dataset2))

# Iterate and print elements of the zipped dataset
for d1, d2 in zipped_dataset:
    print(d1.numpy(), d2.numpy())
