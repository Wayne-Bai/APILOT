
import tensorflow as tf

def convolution(input_tensor, filter_tensor, strides, padding):
    # Create a 2-D convolution operation using raw ops.
    # The first dimension of the input and filter tensors is assumed to be the batch dimension.
    # The second and third dimensions are assumed to be the height and width dimensions, respectively.
    # The fourth dimension is assumed to be the channel dimension.
    
    # Extract the batch size from the input tensor shape.
    batch_size = tf.shape(input_tensor)[0]
    
    # Calculate the output shape by applying strides to the input shape.
    out_height, out_width = (tf.shape(input_tensor)[1] - filter_tensor.shape[0]) // strides[1], \
                            (tf.shape(input_tensor)[2] - filter_tensor.shape[1]) // strides[2]
    output_shape = tf.TensorShape([batch_size, out_height, out_width, filter_tensor.shape[-1]])
    
    # Create a 2-D convolution operation using raw ops.
    # The first dimension is the batch size, the second and third dimensions are the height and width dimensions, respectively.
    # The fourth dimension is the channel dimension.
    conv_op = tf.raw_ops.Conv2D(input=input_tensor, filter=filter_tensor, strides=strides, padding=padding)
    
    # Reshape the output of the convolution operation to match the desired output shape.
    output = tf.reshape(conv_op, output_shape)
    
    return output
