import tensorflow as tf

# Create two example datasets
dataset1 = tf.data.Dataset.from_tensor_slices([1, 2, 3])
dataset2 = tf.data.Dataset.from_tensor_slices([4, 5, 6])

# Function to zip the datasets
def create_zip_dataset(dataset1, dataset2):
    return tf.data.Dataset.zip((dataset1, dataset2))

# Usage
zipped_dataset = create_zip_dataset(dataset1, dataset2)

# To iterate through the zipped dataset
for element in zipped_dataset:
    print(element)

# Alternatively, you can iterate over the dataset pairs directly
for tuple_elements in zipped_dataset:
    print(tuple_elements)
