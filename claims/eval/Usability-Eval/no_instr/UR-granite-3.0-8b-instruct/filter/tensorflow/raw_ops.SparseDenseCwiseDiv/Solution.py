import tensorflow as tf

# Assuming sp and dense are your SparseTensor and dense Tensor respectively
# sp = tf.SparseTensor(...)
# dense = tf.constant(...)

# Component-wise division of SparseTensor by dense Tensor
divided_sp = tf.raw_ops.SparseSegmentDivide(sp=sp, dense_shape=tf.shape(sp), segment_ids=tf.range(tf.size(sp)), num_segments=tf.size(dense))
