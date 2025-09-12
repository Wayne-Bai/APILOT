
import tensorflow as tf

input = tf.constant([[
    [[1], [2], [4], [5]],
    [[1], [3], [5], [7]],
    [[2], [4], [7], [9]],
    [[3], [5], [10], [11]]
]], tf.float32)

size = [1, 2, 2, 1]
strides = [1, 2, 2, 1]
half_pixel_centers = True

result = tf.raw_ops.FractionalAvgPool(value=input, pooling_ratio=[1.0, 1.44, 1.44, 1.0], pseudo_random=0, overlapping=False, deterministic=False, seed=0, seed2=0)

print(result)
