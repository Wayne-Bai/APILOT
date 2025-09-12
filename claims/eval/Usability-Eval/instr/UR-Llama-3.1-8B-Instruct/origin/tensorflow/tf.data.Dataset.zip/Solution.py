# Import necessary libraries
import tensorflow as tf
import numpy as np

# Create two example datasets
dataset1 = tf.data.Dataset.from_tensor_slices(np.random.rand(10))
dataset2 = tf.data.Dataset.from_tensor_slices(np.random.rand(10))

# Stack the datasets together
combined_dataset = tf.data.Dataset.zip((dataset1, dataset2))

# Print the shape of the combined dataset
print(combined_dataset.output_types)
print(combined_dataset.output_shapes)

# Iterate over the combined dataset
for feature1, feature2 in combined_dataset.take(5):
    print(feature1.numpy(), feature2.numpy())

# Alternatively, you can use the Dataset interleave function
interleaved_dataset = tf.data.Dataset.interleave(
    (dataset1, dataset2),
    cycle_length=2,
    num_parallel_calls=tf.data.AUTOTUNE,
)

# Iterate over the interleaved dataset
for feature in interleaved_dataset.take(10):
    print(feature)
