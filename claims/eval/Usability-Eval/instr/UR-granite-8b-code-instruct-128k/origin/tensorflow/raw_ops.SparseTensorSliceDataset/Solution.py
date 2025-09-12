import tensorflow as tf

# Example usage
sparse_tensor = tf.SparseTensor(indices=[[0, 0]], values=[1], dense_shape=[1, 1])
dataset = tf.data.Dataset.from_sparse_tensor_slices(sparse_tensor)
for element in dataset:
    print(element)
