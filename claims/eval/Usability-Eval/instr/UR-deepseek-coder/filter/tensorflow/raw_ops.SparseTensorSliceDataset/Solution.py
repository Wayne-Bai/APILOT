import tensorflow as tf

def split_sparse_tensor(sparse_tensor):
    # Get the shape of the SparseTensor
    shape = sparse_tensor.dense_shape
    
    # Create a dataset from the SparseTensor's values
    values_dataset = tf.data.Dataset.from_tensor_slices(sparse_tensor.values)
    
    # Create a dataset from the SparseTensor's indices
    indices_dataset = tf.data.Dataset.from_tensor_slices(sparse_tensor.indices)
    
    # Zip the values and indices datasets together
    dataset = tf.data.Dataset.zip((values_dataset, indices_dataset))
    
    # Map the dataset to create a tuple of (value, index) for each row
    def map_fn(value, index):
        return value, index
    
    dataset = dataset.map(map_fn)
    
    return dataset

# Example usage:
# Create a SparseTensor
indices = tf.constant([[0, 0], [1, 2], [2, 3]], dtype=tf.int64)
values = tf.constant([1, 2, 3], dtype=tf.int32)
dense_shape = tf.constant([3, 4], dtype=tf.int64)
sparse_tensor = tf.SparseTensor(indices, values, dense_shape)

# Split the SparseTensor into elements row-wise
dataset = split_sparse_tensor(sparse_tensor)

# Iterate over the dataset
for element in dataset:
    print(element)
