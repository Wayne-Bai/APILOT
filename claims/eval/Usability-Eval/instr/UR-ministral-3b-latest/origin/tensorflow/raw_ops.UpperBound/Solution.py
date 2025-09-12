import tensorflow as tf

def apply_upper_bound(sorted_values, values):
    def upper_bound(values):
        return tf.nn.top_k(values, int(values.get_shape()[1]), sorting_axis=1, name='upper_bound')

    return upper_bound(sorted_values)

sorted_values = tf.raw_ops.create([0, 3, 5], [tf.constant([1, 2, 4], dtype=tf.int64), tf.constant([5, 6, 3], dtype=tf.int64)])

values = tf.raw_ops.create([0, 1], [tf.constant([3, 5], dtype=tf.int64), tf.constant([4, 5], dtype=tf.int64)])

output = apply_upper_bound(sorted_values, values)
print(output)
