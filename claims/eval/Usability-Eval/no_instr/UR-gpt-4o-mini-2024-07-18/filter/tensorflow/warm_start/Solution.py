import tensorflow as tf

# Function to create a dataset with prefetching enabled
def create_dataset(data, buffer_size=1):
    dataset = tf.data.Dataset.from_tensor_slices(data)
    dataset = dataset.prefetch(buffer_size=tf.data.AUTOTUNE)  # Use AUTOTUNE or set a specific buffer size
    return dataset

# Example usage
data = [i for i in range(100)]
dataset = create_dataset(data)

# Create an iterator
iterator = iter(dataset)

# Retrieve elements from the iterator
for _ in range(5):
    print(next(iterator))
