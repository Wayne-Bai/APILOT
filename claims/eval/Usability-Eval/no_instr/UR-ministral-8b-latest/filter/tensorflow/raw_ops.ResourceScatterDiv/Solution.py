import tensorflow as tf

# Define a sparse matrix and a variable
sparse_matrix = tf.sparse.SparseTensor(tf.constant([0, 0, 1, 1], dtype=tf.int64),
                                      tf.constant([1, 2, 3, 4], dtype=tf.float32),
                                      tf.constant([2, 2, 2, 2], dtype=tf.int64))
resource_variable = tf.Variable(sparse_matrix, dtype=tf.float32)

# Define a sparse input matrix
sparse_input = tf.SparseTensor(tf.constant([0, 1, 1, 2], dtype=tf.int64),
                               tf.constant([0.5, 2.5, 3.5, 4.5], dtype=tf.float32),
                               tf.constant([2, 2, 2, 2], dtype=tf.int64))

@tf.raw_ops.Rawer
def custom_divide_sparse(resource):
    consistent_output = None
    resource_program = resource[0]
    variable_program = resource[1]
    input_program = resource[2]

    output = tf.raw_ops.SparseDivide()
    output.result()
    consistent_output = tf.raw_ops.SparseGather()
    consistent_output.result()
    return [consistent_output.output, output, variable_program]

sparse_update = custom_divide_sparse([resource_variable.handle, resource_variable.handle])

with tf.compat.v1.Session() as sess:
    sess.run(tf.compat.v1.global_variables_initializer())
    _, output = sess.run([sparse_update, sparse_update])
    print(output)
