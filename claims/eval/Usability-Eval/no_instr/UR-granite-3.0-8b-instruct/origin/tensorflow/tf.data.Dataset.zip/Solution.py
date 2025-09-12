import tensorflow as tf

# Assuming you have two datasets, dataset1 and dataset2
# Replace the following lines with your actual datasets
dataset1 = tf.data.Dataset.from_tensor_slices([1, 2, 3])
dataset2 = tf.data.Dataset.from_tensor_slices([4, 5, 6])

# Create a Dataset that zips together dataset1 and dataset2
zipped_dataset = tf.data.Dataset.zip((dataset1, dataset2))

# Print the zipped dataset
for element in zipped_dataset:
    print(element)
