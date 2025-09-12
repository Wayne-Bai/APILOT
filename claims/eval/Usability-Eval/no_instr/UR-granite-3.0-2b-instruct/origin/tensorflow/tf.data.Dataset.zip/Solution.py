import tensorflow as tf

# Assuming you have two datasets named dataset1 and dataset2
dataset1 = ...  # define your dataset1
dataset2 = ...  # define your dataset2

# Zip the datasets together
zip_datasets = tf.data.Dataset.zip((dataset1, dataset2))

# Print the first element of the zipped dataset
for element in zip_datasets.take(1):
    print(element)
