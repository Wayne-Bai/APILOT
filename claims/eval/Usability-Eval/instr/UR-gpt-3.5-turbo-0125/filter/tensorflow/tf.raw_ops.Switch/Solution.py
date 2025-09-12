
import tensorflow as tf

pred = tf.constant(True)
data = tf.constant(5.0)

output = tf.raw_ops.Method(data=data, pred=pred)

print(output)
