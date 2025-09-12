import tensorflow as tf

# Define the input tensor (e.g., a batch of images)
# Shape: [batch, height, width, channels]
input_tensor = tf.constant([
    [[
        [1.0], [2.0], [3.0],
        [4.0], [5.0]
    ]],
    [[
        [6.0], [7.0], [8.0],
        [9.0], [10.0]
    ]]
], dtype=tf.float32)

# Define the filter/kernel tensor
# Shape: [filter_height, filter_width, in_channels, out_channels]
kernel = tf.constant([
    [[[1.0]], [[0.0]]],
    [[[0.0]], [[1.0]]]
], dtype=tf.float32)

# Define stride and padding
strides = [1, 1, 1, 1]  # Must be 1-D of length 4
padding = 'SAME'  # Padding type, can be 'VALID' or 'SAME'

# Perform 2-D convolution using the tf.nn.conv2d function
output = tf.nn.conv2d(input_tensor, kernel, strides=strides, padding=padding)

print("Output of convolution:")
print(output.numpy())
