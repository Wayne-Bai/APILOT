import tensorflow as tf

def conv2d(input_tensor, filter_tensor, strides, padding):
    # Ensure the input and filter tensors are 4D
    input_tensor = tf.convert_to_tensor(input_tensor, dtype=tf.float32)
    filter_tensor = tf.convert_to_tensor(filter_tensor, dtype=tf.float32)
    
    # Ensure strides is a list of length 4
    if len(strides) != 4:
        raise ValueError("Strides must be a list of length 4")
    
    # Perform the convolution operation
    conv_output = tf.nn.conv2d(
        input=input_tensor,
        filters=filter_tensor,
        strides=strides,
        padding=padding.upper()
    )
    
    return conv_output

# Example usage:
# input_tensor = tf.random.normal([1, 28, 28, 3])  # [batch, height, width, channels]
# filter_tensor = tf.random.normal([5, 5, 3, 16])  # [filter_height, filter_width, in_channels, out_channels]
# strides = [1, 1, 1, 1]
# padding = 'SAME'
# output = conv2d(input_tensor, filter_tensor, strides, padding)
# print(output)
