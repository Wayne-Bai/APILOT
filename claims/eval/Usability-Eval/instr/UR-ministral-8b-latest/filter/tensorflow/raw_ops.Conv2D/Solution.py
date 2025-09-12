import tensorflow as tf
import numpy as np

# Define the method to perform 2D convolution using tf.raw_ops
def custom_conv2d(input_tensor, filter_tensor, strides=(1, 1), padding='same', data_format='NHWC'):
    input_tensor = tf.convert_to_tensor(input_tensor, dtype=tf.float32)
    filter_tensor = tf.convert_to_tensor(filter_tensor, dtype=tf.float32)

    # Assuming the old tensors for the RawOp requires certain dimensions
    input_shape = tf.shape(input_tensor)
    filter_shape = tf.shape(filter_tensor)

    # Assuming a 2D output tensor for the filter shape
    filter_conv_out_shape = tf.TensorShape([filter_shape[1], filter_shape[2]])

    # Query `tf.raw_ops.Conv2D` with necessary parameters
    output_tensor = tf.raw_ops.Conv2D(
        input=input_tensor,
        filters=filter_tensor,
        strides=strides,
        padding=padding,
        data_format=data_format
    )

    return output_tensor

# Example usage
input_data = np.array([[1.0, 2.0], [3.0, 4.0]])
filter = np.array([[1.0, 2.0], [3.0, 4.0]])

input_tensor = tf.constant(input_data)
filter_tensor = tf.constant(filter)

output = custom_conv2d(input_tensor, filter_tensor)
print(output.numpy())
