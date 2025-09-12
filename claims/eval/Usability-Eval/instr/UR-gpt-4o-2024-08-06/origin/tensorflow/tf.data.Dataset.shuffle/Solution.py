import tensorflow as tf

# Example input data
features = tf.constant([[1, 2],
                        [3, 4],
                        [5, 6],
                        [7, 8]])
labels = tf.constant([0, 1, 0, 1])

# Combine the features and labels
dataset = tf.data.Dataset.from_tensor_slices((features, labels))

# Shuffle the dataset
shuffled_dataset = dataset.shuffle(buffer_size=4, seed=42)

# Iterate and print the shuffled dataset
for feature, label in shuffled_dataset:
    print("Feature:", feature.numpy(), "Label:", label.numpy())
