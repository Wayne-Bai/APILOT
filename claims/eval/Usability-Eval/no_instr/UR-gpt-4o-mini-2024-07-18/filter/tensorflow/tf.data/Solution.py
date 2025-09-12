import tensorflow as tf

# Example of using the tf.data API to create a simple dataset
def create_dataset(data, batch_size):
    # Create a TensorFlow dataset from the data
    dataset = tf.data.Dataset.from_tensor_slices(data)
    
    # Shuffle the dataset and create batches
    dataset = dataset.shuffle(buffer_size=len(data)).batch(batch_size)
    
    return dataset

# Sample data
data = [1, 2, 3, 4, 5]

# Create a dataset with batch size of 2
batch_size = 2
dataset = create_dataset(data, batch_size)

# Iterate through the dataset and print the batches
for batch in dataset:
    print(batch.numpy())
