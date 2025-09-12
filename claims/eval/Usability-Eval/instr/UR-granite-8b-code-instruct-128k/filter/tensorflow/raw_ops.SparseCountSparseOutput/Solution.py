import tensorflow as tf

# Create a sparse tensor input
values = [1, 2, 3, 4, 5]
indices = [[0], [2], [4], [6], [8]]
shape = [10]
sparse_tensor = tf.sparse.SparseTensor(indices, values, shape)

# Perform sparse-output bin counting
bins = tf.raw_ops.Bincount(arr=sparse_tensor, size=10)

# Print the result
with tf.Session() as sess:
    result = sess.run(bins)
    print(result)
