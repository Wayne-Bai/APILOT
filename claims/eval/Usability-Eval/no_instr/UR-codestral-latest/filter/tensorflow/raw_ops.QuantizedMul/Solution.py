import tensorflow as tf

# Defining the tensors
x = tf.constant([1, 2, 3], dtype=tf.qint32)
y = tf.constant([2, 3, 4], dtype=tf.qint32)

# Using tf.raw_ops.QuantizedMul
result = tf.raw_ops.QuantizedMul(x=x, y=y, min_x=0, max_x=5, min_y=0, max_y=5, Toutput=tf.qint32)

# Running the calculation
with tf.Session() as sess:
    output = sess.run(result)
    print(output)
