import tensorflow as tf

# Define the FractionalMaxPool function
def fractional_max_pool(input, fraction):
    batch_size, height, width, channels = input.shape.as_list()
    output_height = height * fraction
    output_width = width * fraction
    output = tf.zeros([batch_size, output_height, output_width, channels])

    for i in range(batch_size):
        for j in range(0, height, fraction):
            for k in range(0, width, fraction):
                max_val = tf.reduce_max(input[i, j:j+fraction, k:k+fraction, :])
                output[i, int(j / fraction), int(k / fraction), :] = max_val

    return output

# Compute the gradient of the FractionalMaxPool function
def compute_gradient(input, fraction):
    grad = tf.zeros_like(input)
    grad = tf.raw_ops.FractionalMaxPoolGrad(input, grad, fraction)
    return grad
