
import tensorflow as tf

# Input tensor
x = tf.random.normal(shape=(3, 4, 5))

# Pool window size
pool_size = 2

# Output tensor
y = tf.raw_ops.FractionalMaxPool(x, pool_size, strides=pool_size, padding='VALID')
