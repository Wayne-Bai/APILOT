import tensorflow as tf

# Define a function to create a dataset from a list of numpy arrays
def create_dataset(data_list):
    # Convert the list of numpy arrays to a TensorFlow dataset
    dataset = tf.data.Dataset.from_tensor_slices(data_list)
    # Shuffle the dataset
    dataset = dataset.shuffle(buffer_size=len(data_list))
    # Batch the dataset
    dataset = dataset.batch(batch_size=32)
    return dataset

# Example usage
data_list = [tf.constant(i) for i in range(100)]
dataset = create_dataset(data_list)
