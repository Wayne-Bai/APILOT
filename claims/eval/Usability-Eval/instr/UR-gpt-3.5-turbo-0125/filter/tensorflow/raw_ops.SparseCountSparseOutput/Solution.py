
import tensorflow as tf

# Create a function that performs sparse-output bin counting for a sparse tensor input
def sparse_count(sparse_indices, num_classes):
    output = tf.raw_ops.DenseToSparseBincount(sparse_indices=sparse_indices, num_classes=num_classes)
    return output

# Test the function with sample inputs
sparse_indices = tf.SparseTensor(indices=[[0, 2], [1, 3], [2, 1]], values=[1, 1, 1], dense_shape=[3, 4])
num_classes = 4
result = sparse_count(sparse_indices, num_classes)

print(result)
