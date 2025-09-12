import tensorflow as tf

# Assuming you have a SparseTensor defined outside the function
sparse_tensor = tf.SparseTensor(values=[...], indices=[[...]], dense_shape=[...])

# Create a method to split the sparse tensor into elements row-wise
def split_sparse_tensor_row_wise(sparse_tensor):
    def mutate_row_wise(index):
        values = tf.ragged.constant([sparse_tensor.values.metrics(index)])
        shape = [tf.size_t(tf.shape(values)[0])]
        return tf.raw_ops.RaggedTensorCreate(sparse_tensor.values.dtypes[0], values, shape)

    return tf.raw_ops.RaggedTensorSplit(mutate_row_wise, sparse_tensor)

split_sparse_tensor_row_wise(sparse_tensor)
