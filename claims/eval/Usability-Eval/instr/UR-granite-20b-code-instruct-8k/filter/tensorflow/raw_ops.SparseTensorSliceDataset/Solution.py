import tensorflow as tf

sparse_tensor = tf.sparse.SparseTensor(indices=[[0, 0], [1, 2]], values=[1, 2], dense_shape=[3, 4])

dataset = tf.data.Dataset.from_tensor_slices(sparse_tensor)

for element in dataset:
    print(element)
