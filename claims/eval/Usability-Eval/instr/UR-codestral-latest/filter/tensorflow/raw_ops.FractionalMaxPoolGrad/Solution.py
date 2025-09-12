import tensorflow as tf

# To create a custom gradient for FractionalMaxPool function,
# create a function that first calculates the forward pass for FractionalMaxPool
# and then calculates and returns the gradient for it.
def custom_grad_fractional_max_pool(inputs, ksize, strides, output_shape):
    # Forward pass: FractionalMaxPool
    def fractional_max_pool(x):
        return tf.nn.fractional_max_pool(x, ksize, strides, output_shape)

    # Calculating and returning gradient for FractionalMaxPool using GradientTape
    with tf.GradientTape() as tape:
        tape.watch(inputs)
        output = fractional_max_pool(inputs)
    grads = tape.gradient(output, inputs)
    return grads
