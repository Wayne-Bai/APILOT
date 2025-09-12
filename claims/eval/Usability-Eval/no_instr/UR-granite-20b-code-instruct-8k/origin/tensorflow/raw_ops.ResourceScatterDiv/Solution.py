import tensorflow as tf

def sparse_div_example():
    # Create a variable with random initial values
    var = tf.Variable([1.0, 2.0, 3.0])

    # Create a sparse tensor to divide
    sparse_tensor = tf.SparseTensor(indices=[[0, 0], [1, 1]], values=[4.0, 5.0], dense_shape=[2, 2])

    # Use tf.raw_ops. sparse_div to divide the sparse updates into the variable
    updated_var = tf.raw_ops.SparseDiv(sparse_indices=sparse_tensor.indices,
                                       sparse_values=sparse_tensor.values,
                                       sparse_shape=sparse_tensor.dense_shape,
                                       dense=var)

    # Initialize and run the variable initializer
    init = tf.global_variables_initializer()
    with tf.Session() as sess:
        sess.run(init)

        # Print the initial variable values
        print("Initial variable values:", sess.run(var))

        # Print the updated variable values
        print("Updated variable values:", sess.run(updated_var))

if __name__ == "__main__":
    sparse_div_example()
