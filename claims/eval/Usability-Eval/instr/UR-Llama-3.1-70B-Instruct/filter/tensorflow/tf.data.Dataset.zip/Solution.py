import tensorflow as tf

# Create two sample datasets
dataset1 = tf.data.Dataset.from_tensor_slices([1, 2, 3])
dataset2 = tf.data.Dataset.from_tensor_slices(['a', 'b', 'c'])

# Use the zip method to combine the datasets
zipped_dataset = tf.data.Dataset.zip((dataset1, dataset2))

# Print the zipped dataset
for element in zipped_dataset:
    print(element)
    
# Outputs:
# (1, 'a')
# (2, 'b')
# (3, 'c')

# Creating the zipped dataset with more than two datasets
dataset3 = tf.data.Dataset.from_tensor_slices([True, False, True])
zipped_dataset_with_three_datasets = tf.data.Dataset.zip((dataset1, dataset2, dataset3))

# Print the zipped dataset with three components
for element in zipped_dataset_with_three_datasets:
    print(element)
    
# Outputs:
# (1, 'a', True)
# (2, 'b', False)
# (3, 'c', True)
