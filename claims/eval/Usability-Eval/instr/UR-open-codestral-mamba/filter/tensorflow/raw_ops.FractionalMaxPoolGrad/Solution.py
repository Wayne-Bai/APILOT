import tensorflow as tf

# Create an input tensor to compute the gradient for.
input_tensor = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], dtype=tf.float32)

# Create the underlying function object.
pool = tf.raw_ops.FractionalMaxPool(
    input=input_tensor,
    pooling_ratio=0.75,
    pseudo_random=True,
    overlapping=True,
    seed=0,
    padding='VALID',
)

# Get the gradients for the tensor input
input_tensor_grad = tf.gradients(pool, input_tensor)

# Printing the gradient
print(input_tensor_grad)
