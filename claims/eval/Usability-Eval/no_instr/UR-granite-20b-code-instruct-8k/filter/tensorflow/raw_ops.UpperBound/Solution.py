
import tensorflow as tf

# upper_bound(sorted_search_values, values) along each row.
# Input:
#   sorted_search_values: A Tensor with type float32.
#     N x>= 1 matrix, sorted in descending order along each row.
#   values: A Tensor with type float32.
#     N x 1 matrix.
# Output:
#   a Tensor with type int32.
#     N x 1 matrix that has the same numbers of rows as values, where output[i][0]
#     is the index in the i-th row of the tensor values that is equal to
#     sorted_search_values[i][0]. If there is no such index, the result is
#     considered to be -1.
result = tf.raw_ops.UpperBound(sorted_search_values=sorted_search_values, values=values)
