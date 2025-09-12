# Import necessary libraries
import tensorflow as tf

# Create sample datasets
dataset1 = tf.data.Dataset.from_tensor_slices([1, 2, 3, 4, 5])
dataset2 = tf.data.Dataset.from_tensor_slices(['a', 'b', 'c', 'd', 'e'])

# Use zip to create a combined dataset
combined_dataset = tf.data.Dataset.zip((dataset1, dataset2))

# Print the combined dataset
for x, y in combined_dataset:
    print(f"Element: {x}, Label: {y}")
