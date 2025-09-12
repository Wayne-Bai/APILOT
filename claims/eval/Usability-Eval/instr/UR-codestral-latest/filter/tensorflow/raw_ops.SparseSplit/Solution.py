import tensorflow as tf

# Define a 2D SparseTensor
indices = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1]]
values = [1, 2, 3, 4, 5]
dense_shape = [3, 3]
sparse_tensor = tf.SparseTensor(indices, values, dense_shape)

# Split the SparseTensor along the second dimension
num_split = 2
splitted_sparse_tensor = tf.sparse.split(sparse_tensor, num_split, axis=1)

# To confirm if the split operation is done correctly, start a TensorFlow session
with tf.Session() as sess:
    print(sess.run(splitted_sparse_tensor))
