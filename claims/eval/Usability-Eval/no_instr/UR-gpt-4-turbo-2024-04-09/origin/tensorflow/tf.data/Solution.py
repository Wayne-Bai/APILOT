import tensorflow as tf

# Various utilities under tf.data can be used to handle data effectively for building machine learning models

# Example of using tf.data.Dataset for batching, shuffling, and iterating through data.

# Sample data: features and labels
features = [1.0, 2.0, 3.0, 4.0, 5.0]
labels = [0, 1, 0, 1, 0]

# Create a Dataset object
dataset = tf.data.Dataset.from_tensor_slices((features, labels))

# Shuffle, batch, and repeat
dataset = dataset.shuffle(buffer_size=5).batch(2).repeat(2)

# Iterate over the dataset
for batch_features, batch_labels in dataset:
    print(f"Features: {batch_features} Labels: {batch_labels}")
