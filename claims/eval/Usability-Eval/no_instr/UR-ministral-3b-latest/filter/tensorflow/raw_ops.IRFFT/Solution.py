import tensorflow as tf
# Creating constant tensor
const_tensor = tf.constant([[1, 2, 3], [4, 5, 6]], dtype=tf.complex64)

# Defining the tensor as input
input_tensor = tf.raw_ops.method(inputs=const_tensor,
                                 op=tf.raw_opsowali.fast_fourier_transform,
                                 scale=1)

# Doing the Inverse real-valued fast Fourier transform
inverse_tensor = input_tensor

# Print the inverse tensor
print(inverse_tensor)