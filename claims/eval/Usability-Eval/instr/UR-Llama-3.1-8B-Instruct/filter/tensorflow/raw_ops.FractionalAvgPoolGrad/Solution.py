# Import necessary modules
import tensorflow as tf

# Define the variables
input_tensor = tf.random.normal([1, 10, 10, 32])  # input tensor
stride = [1, 2, 2, 1]  # stride
pooling_size = [3, 3]  # pooling size
p = 0.5  # dropout probability

# Compute the FractionalAvgPool
fractional_avg_pool = tf.image.resize(tf.nn.avg_pool(input_tensor, ksize=[1, pooling_size[0], pooling_size[1], 1],
                                                    strides=[1, stride[1], stride[2], 1],
                                                    padding='VALID'), size=tf.cast([2*stride[1], 2*stride[2]], tf.float32),
                                            method='bilinear', antialias=True)

# Compute the gradient of the FractionalAvgPool using the backward function from GradientTape
with tf.GradientTape() as tape:
    # Record the computation of the backward pass.
    output = fractional_avg_pool

# Get the gradients of the loss with respect to the input tensor
gradients = tape.gradient(output, input_tensor)

# Reshape the gradients to the original shape
gradients = tf.reshape(gradients, input_tensor.shape)

print(gradients)
