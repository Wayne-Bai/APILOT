
import tensorflow as tf

# Define the input tensor and the corresponding gradients
input_tensor = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
gradients = tf.constant([[1.0, 1.0], [1.0, 1.0]])

# Compute the gradients of the maxpooling function
grads = tf.raw_ops.MaxPoolGrad(input=input_tensor,
                               grad=gradients,
                               ksize=[1, 2, 2, 1],
                               strides=[1, 2, 2, 1],
                               padding='SAME')

# Print the resulting gradients
print(grads)
