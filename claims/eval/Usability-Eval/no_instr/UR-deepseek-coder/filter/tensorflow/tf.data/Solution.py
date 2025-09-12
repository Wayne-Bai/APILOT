import tensorflow as tf

# Example of using tf.data.Dataset API
def create_dataset(data, labels):
    dataset = tf.data.Dataset.from_tensor_slices((data, labels))
    dataset = dataset.shuffle(buffer_size=1000).batch(32).prefetch(tf.data.experimental.AUTOTUNE)
    return dataset

# Example usage
data = tf.random.normal([1000, 10])
labels = tf.random.uniform([1000], maxval=10, dtype=tf.int32)

dataset = create_dataset(data, labels)

# Iterate over the dataset
for features, label in dataset.take(5):
    print(features, label)
