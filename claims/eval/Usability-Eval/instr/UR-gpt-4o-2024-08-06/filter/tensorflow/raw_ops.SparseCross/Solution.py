import tensorflow as tf

# Function to generate a sparse cross from sparse and dense tensors
def generate_sparse_cross(sparse_tensors, dense_tensors, num_buckets, hashed_output=True):
    # Convert sparse tensors to SparseTensor
    sparse_tensor_objects = [
        tf.sparse.SparseTensor(indices=sparse.indices, values=sparse.values, dense_shape=sparse.dense_shape) 
        for sparse in sparse_tensors
    ]

    # Generate sparse cross
    sparse_cross_output = tf.raw_ops.SparseCross(
        indices=[s.indices for s in sparse_tensor_objects],
        values=[s.values for s in sparse_tensor_objects],
        shapes=[tf.convert_to_tensor(s.dense_shape, dtype=tf.int64) for s in sparse_tensor_objects],
        dense_inputs=dense_tensors,
        num_buckets=num_buckets,
        hash_key=0,  # Default value for compatibility
        hashed_output=hashed_output
    )
    return sparse_cross_output

# Example of creating sparse and dense tensors
sparse_tensors_example = [
    tf.sparse.SparseTensor(indices=[[0, 0], [1, 2]], values=[3, 4], dense_shape=[3, 3]),
    tf.sparse.SparseTensor(indices=[[0, 1], [2, 2]], values=[5, 9], dense_shape=[3, 3])
]

dense_tensors_example = [
    tf.constant([[1, 2], [3, 4], [5, 6]], dtype=tf.int64)
]

# Generating sparse cross from the example tensors
sparse_cross_output = generate_sparse_cross(sparse_tensors_example, dense_tensors_example, num_buckets=100)
print(sparse_cross_output)
