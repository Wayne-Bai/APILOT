import tensorflow as tf

# Example input tensor
x = tf.constant([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]], dtype=tf.float32)

# Example kernel for max pooling, fixed-size window with stride 2
kernel = tf.constant([[1.0]], dtype=tf.float32)

# Example max pooling operation
max_pooling = tf.raw_ops.MaxPool(
    input=x,
    filter_shape=kernel.shape,
    strides=tf.constant([[1, 2], [2, 1]], dtype=tf.int32),
    padding='VALID'
)

# Compute gradients of the max pooling with respect to the input
grads = tf.raw_ops.Gradient(multi_input_op=tf.raw_ops.MaxPool,
                            inputs=[x, kernel])

# Define a mini-batch of samples to compute the gradient
samples = tf.range(x.shape[0].numpy())

# Print gradients (for each sample in the minibatch)
with tf.GradientTape() as tape:
    tape.watch(x)
    output = max_pooling

gradients = tape.gradient(output, x)

for i, g in enumerate(gradients):
    print(f"Gradient for sample {samples[i]}: {g.numpy()}")
