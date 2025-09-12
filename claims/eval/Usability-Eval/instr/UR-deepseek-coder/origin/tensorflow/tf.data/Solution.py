import tensorflow as tf

# Example usage of tf.data.Dataset
def create_dataset(data, labels):
    dataset = tf.data.Dataset.from_tensor_slices((data, labels))
    return dataset

# Example data
data = tf.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
labels = tf.constant([0, 1, 0])

# Create dataset
dataset = create_dataset(data, labels)

# Example of batching and prefetching
batched_dataset = dataset.batch(2).prefetch(tf.data.experimental.AUTOTUNE)

# Iterate over the dataset
for features, label in batched_dataset:
    print("Features:", features.numpy())
    print("Label:", label.numpy())
