import tensorflow as tf

# Define a function to reverse a tensor along a given axis
def reverse(tensor, axis):
    # Get the shape of the input tensor
    shape = tensor.shape.as_list()
    
    # Reverse the tensor along the specified axis
    reversed_tensor = tf.reverse(tensor, [axis])
    
    # Reshape the tensor to its original shape
    return tf.reshape(reversed_tensor, shape)
