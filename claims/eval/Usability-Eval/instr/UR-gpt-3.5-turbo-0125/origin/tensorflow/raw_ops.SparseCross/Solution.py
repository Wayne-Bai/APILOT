
import tensorflow as tf

# Generate sparse cross from a list of sparse and dense tensors
def generate_sparse_cross(sparse_tensors, dense_tensors):
    sparse_cross = tf.raw_ops.SparseCross(inputs=sparse_tensors,dense_inputs=dense_tensors)
    return sparse_cross
