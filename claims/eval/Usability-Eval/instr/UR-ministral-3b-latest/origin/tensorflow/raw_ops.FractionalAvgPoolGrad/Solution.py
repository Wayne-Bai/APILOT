import tensorflow as tf

# Define the input tensor and the gradient output tensor
input_tensor = tf.constant([[1.0, 2.0, 3.0]])
gradient_output_tensor = tf.raw_ops.FractionalAvgPoolGrad(input_tensor, ksize=tf.constant([2, 2]))

# When using raw_ops, ensure to specify the input tensor and the size of the ksize array
# Compute the gradient
gradient = tf.raw_ops.FractionalAvgPoolGrad.apply(
    input_tensors=[input_tensor],
    ksize=[2, 2],
    output_shape=[input_tensor.shape.as_list()[:-2]])

print(gradient.numpy())
