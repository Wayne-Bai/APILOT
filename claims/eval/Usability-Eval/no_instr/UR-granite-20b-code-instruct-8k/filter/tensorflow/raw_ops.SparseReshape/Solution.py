import tensorflow as tf

# Reshapes a SparseTensor to represent values in a new dense shape.
#
# Reshapes a `SparseTensor` to represent values in a new dense shape.
#
# Args:
#     sp_input: The input `SparseTensor`.
#     shape: A 1-D (vector) int64 `Tensor` specifying the new dense shape of the
#         sparse tensor.
#     name: A name prefix for the returned tensors (optional).
#
# Returns:
#     A `SparseTensor` with the same values as `sp_input`, but with dense shape
#     `shape`.
#
# @compatibility(eager)
# Eager execution is enabled by default in TensorFlow 2.0.
# For example, `tf.sparse.reshape` is equivalent to:
#
# 