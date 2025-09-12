import tensorflow as tf

# Let's define two simple datasets
dataset1 = tf.data.Dataset.from_tensor_slices(tf.random.uniform([4, 10]))
dataset2 = tf.data.Dataset.from_tensor_slices(tf.random.uniform([4, 10]))

# Zip the datasets together
zipped_dataset = tf.data.Dataset.zip((dataset1, dataset2))

# Print the zipped dataset
for element in zipped_dataset:
    print(element)
