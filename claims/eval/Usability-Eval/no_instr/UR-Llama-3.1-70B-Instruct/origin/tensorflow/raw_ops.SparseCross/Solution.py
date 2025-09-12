import tensorflow as tf
from tensorflow.core.framework import sparse_tensor_pb2

def generate_sparse_cross():
    # Create a sparse tensor
    sparse_tensor_1 = sparse_tensor_pb2.SparseTensor()
    sparse_tensor_1.values.extend([1, 2])
    sparse_tensor_1.indices.extend([[0, 0], [1, 0]])
    sparse_tensor_1.dense_shape.extend([2, 1])

    sparse_tensor_2 = sparse_tensor_pb2.SparseTensor()
    sparse_tensor_2.values.extend([3, 4])
    sparse_tensor_2.indices.extend([[0, 0], [1, 0]])
    sparse_tensor_2.dense_shape.extend([2, 1])

    dense_tensor = tf.constant([[1, 2], [3, 4]])

    sparse_cross = tf.raw_ops.SparseCross(
        sparse_indices=[sparse_tensor_1.indices, sparse_tensor_2.indices],
        sparse_values=[sparse_tensor_1.values, sparse_tensor_2.values],
        sparse_shapes=[sparse_tensor_1.dense_shape, sparse_tensor_2.dense_shape],
        dense_inputs=[dense_tensor],
        num_buckets=100,
        hash_key=5,
        name="SparseCross"
    )

    return sparse_cross

# Example usage
sparse_cross = generate_sparse_cross()

with tf.Session() as sess:
    output = sess.run(sparse_cross)
    print(output)
