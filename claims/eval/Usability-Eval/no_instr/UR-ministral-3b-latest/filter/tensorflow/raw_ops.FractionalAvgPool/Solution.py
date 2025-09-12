import tensorflow as tf

def fractional_average_pooling(inputs):
    # Since tf.raw_ops is a deprecated API, let's use the more recent tf.nn element.
    fractional_pool = tf.nn.fractional_max_pool2d
    depth = fractional_pool.value
    size = fractional_pool.prob
    stride_h = fractional_pool.stride_h
    stride_w = fractional_pool.stride_w
    return fractional_pool(inputs, [depth, size], [stride_h, stride_w])

# Example Usage
input_data = tf.random.uniform((1, 16, 16, 3))
output_data = fractional_average_pooling(input_data)

output_data
