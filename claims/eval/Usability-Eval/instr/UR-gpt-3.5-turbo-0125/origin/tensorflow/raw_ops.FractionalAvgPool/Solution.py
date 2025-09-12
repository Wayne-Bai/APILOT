
import tensorflow as tf

def fractional_avg_pool(input, pooling_ratio):
    return tf.nn.fractional_avg_pool(input, pooling_ratio, deterministic=False)

# Example usage
input = tf.constant([[[[1.0],[2.0],[3.0],[4.0]],
                      [[5.0],[6.0],[7.0],[8.0]],
                      [[9.0],[10.0],[11.0],[12.0]],
                      [[13.0],[14.0],[15.0],[16.0]]]], dtype=tf.float32)

pooling_ratio = [1.0, 2.0, 2.0, 1.0]

output, _, _ = fractional_avg_pool(input=input, pooling_ratio=pooling_ratio)

with tf.Session() as sess:
    result = sess.run(output)
    print(result)
