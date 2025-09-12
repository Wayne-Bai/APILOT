import tensorflow as tf

def split_sparse_tensor(sparse_tensor, num_split, axis=0):
    # Validate the number of splits
    if num_split <= 0 or num_split > sparse_tensor.dense_shape[axis].numpy():
        raise ValueError("num_split must be a positive integer less than or equal to the dimension length.")
    
    # Split the SparseTensor along the specified axis
    return tf.sparse.split(sparse_tensor, num_split, axis)

# Example usage
sparse_tensor = tf.sparse.SparseTensor(
    indices=[[0, 0], [1, 2]],
    values=[1, 2],
    dense_shape=[3, 3]
)

num_split = 3
splits = split_sparse_tensor(sparse_tensor, num_split)

for i, split in enumerate(splits):
    print(f"Split {i}: {split}")
