import tensorflow as tf

def maxpool_grad(input, grad, ksize, strides, padding, data_format="NHWC"):
    # Compute the forward pass of max pooling
    with tf.compat.v1.variable_scope("maxpool_grad"):
        input_shape = tf.shape(input)
        grad_shape = tf.shape(grad)

        # Perform the max pooling operation
        maxpool_output = tf.nn.max_pool(input, ksize=ksize, strides=strides, padding=padding, data_format=data_format)

        # Compute the gradient of the max pooling operation
        maxpool_grad_output = tf.nn.max_pool_with_argmax(input, ksize=ksize, strides=strides, padding=padding, data_format=data_format)

        # Extract the indices from the max_pool_with_argmax output
        _, argmax = maxpool_grad_output

        # Reshape the indices to match the shape of the gradient
        argmax_shape = tf.shape(argmax)
        argmax = tf.reshape(argmax, [-1])

        # Flatten the gradient tensor
        grad_flat = tf.reshape(grad, [-1])

        # Create a sparse tensor from the indices and gradient values
        sparse_grad = tf.SparseTensor(tf.expand_dims(argmax, 1), grad_flat, tf.cast(tf.reduce_prod(argmax_shape), tf.int64))

        # Convert the sparse tensor to a dense tensor
        dense_grad = tf.sparse.to_dense(sparse_grad)

        # Reshape the dense tensor to the original input shape
        dense_grad = tf.reshape(dense_grad, input_shape)

        return dense_grad

# Example usage
input_tensor = tf.constant([[[[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]]])
grad_tensor = tf.constant([[[[1.0], [2.0], [3.0]]]])
ksize = [1, 2, 2, 1]
strides = [1, 1, 1, 1]
padding = "VALID"

result = maxpool_grad(input_tensor, grad_tensor, ksize, strides, padding)
print(result)
