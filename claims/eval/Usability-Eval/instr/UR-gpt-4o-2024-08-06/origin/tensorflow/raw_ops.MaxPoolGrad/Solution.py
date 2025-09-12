import tensorflow as tf

# Define the input tensor
input_tensor = tf.constant([[1.0, 2.0, 3.0, 4.0],
                            [5.0, 6.0, 7.0, 8.0],
                            [9.0, 10.0, 11.0, 12.0],
                            [13.0, 14.0, 15.0, 16.0]],
                           shape=[1, 4, 4, 1])

# Define the kernel size and strides
pool_size = [1, 2, 2, 1]
strides = [1, 2, 2, 1]

# Perform max pooling
max_pooled = tf.nn.max_pool2d(input_tensor, ksize=pool_size, strides=strides, padding='VALID')

# Simulate the gradient of the output (d_out)
d_out = tf.constant([[10.0, 20.0],
                     [30.0, 40.0]],
                    shape=[1, 2, 2, 1])

# Compute the gradient of the max pooling
grad = tf.raw_ops.MaxPoolGrad(
    orig_input=input_tensor,
    orig_output=max_pooled,
    grad=d_out,
    ksize=pool_size,
    strides=strides,
    padding='VALID'
)

print("Input Tensor:")
print(input_tensor.numpy())

print("Max Pooled Output:")
print(max_pooled.numpy())

print("Gradient of Max Pooling:")
print(grad.numpy())
