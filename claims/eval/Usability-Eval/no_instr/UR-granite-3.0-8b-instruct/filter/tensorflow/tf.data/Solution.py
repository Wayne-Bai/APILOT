import tensorflow as tf

# Define a function to create a TensorFlow dataset from a list of numpy arrays
def create_dataset(data, labels):
    # Convert numpy arrays to TensorFlow tensors
    data = tf.convert_to_tensor(data)
    labels = tf.convert_to_tensor(labels)

    # Create a TensorFlow dataset from the tensors
    dataset = tf.data.Dataset.from_tensor_slices((data, labels))

    # Shuffle and batch the dataset
    dataset = dataset.shuffle(buffer_size=1024).batch(32)

    return dataset

# Example usage:
data = np.random.rand(1000, 32)  # 1000 samples, 32 features
labels = np.random.randint(2, size=1000)  # Binary labels

dataset = create_dataset(data, labels)
