import tensorflow as tf
from tensorflow.python.ops import gen_ragged_to_dense_op

# Define the RaggedTensor
rt = tf.ragged.constant([[1, 2, 3, 4], [5, 6], [7, 8, 9]])

# Convert RaggedTensor to SparseTensor
sp = gen_ragged_to_dense_op.RaggedTensorToSparse(
    rt.values, rt.row_splits_dtype(), rt.row_splits)

print(sp)
