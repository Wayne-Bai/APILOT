import tensorflow as tf

def convolution_2d(input_tensor, filter_tensor, strides=1, padding='VALID'):
    return tf.raw_ops.Conv2D(
        input=input_tensor,
        filters=filter_tensor,
        strides=strides,
        padding=padding,
        data_format='NHWC'
    )

# Example usage
input_tensor = tf.random.normal([1, 64, 64, 3])  # Example input tensor
filter_tensor = tf.random.normal([64, 3, 3, 16])  # Example filter tensor
output_tensor = convolution_2d(input_tensor, filter_tensor, strides=[1, 1, 1, 1], padding='SAME')
print(output_tensor)
