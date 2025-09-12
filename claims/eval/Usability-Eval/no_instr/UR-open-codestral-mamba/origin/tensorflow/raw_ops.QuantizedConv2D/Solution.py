import tensorflow as tf
# Define example 4D input and filter tensors
x = tf.constant([[[[1, 2, 3],[4, 5, 6],[7, 8, 9]],
                 [[10, 11, 12],[13, 14, 15],[16, 17, 18]],
                 [[19, 20, 21],[22, 23, 24],[25, 26, 27]]]], dtype=tf.qint32)

filter = tf.constant([[[[0, 1, 2],[3, 4, 5],[6, 7, 8]]]], dtype=tf.qint32)

with tf.compat.v1.Session() as sess:
    # Perform 2D convolution
    result = sess.run(tf.compat.v1.raw_ops.QuantizedConvolution2D(
        input=x,
        filter=filter,
        strides=[1, 1, 1, 1],
        padding="VALID"))

result
