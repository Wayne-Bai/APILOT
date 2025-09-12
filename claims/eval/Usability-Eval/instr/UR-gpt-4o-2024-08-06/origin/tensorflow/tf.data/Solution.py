import tensorflow as tf

# Create a simple dataset example using `tf.data.Dataset`
def create_dataset():
    # Sample data: 1D tensors
    data = [1, 2, 3, 4, 5]
    labels = [0, 0, 1, 1, 0]
    
    # Create a tf.data.Dataset from tensors
    dataset = tf.data.Dataset.from_tensor_slices((data, labels))
    
    # Apply transformations to the dataset
    # Shuffle the dataset
    dataset = dataset.shuffle(buffer_size=5)
    
    # Batch the dataset into batches of 2
    dataset = dataset.batch(2)
    
    # Map a simple function to each element
    dataset = dataset.map(lambda x, y: (tf.square(x), y))
    
    return dataset

# Create dataset
dataset = create_dataset()

# Iterate through the dataset
for data, label in dataset:
    print(f'Data: {data.numpy()}, Label: {label.numpy()}')
