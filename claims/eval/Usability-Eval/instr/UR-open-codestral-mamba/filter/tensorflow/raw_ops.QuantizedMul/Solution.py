import tensorflow as tf

# Define some quantized tensors
input1 = tf.constant(2, dtype=tf.qint8)
input2 = tf.constant(3, dtype=tf.qint8)

# Define the element-wise multiplication operation
mul_op = tf.raw_ops.Mul(x=input1, y=input2)

# print the output
with tf.compat.v1.Session() as sess:
    output = sess.run(mul_op)
    print(output)
