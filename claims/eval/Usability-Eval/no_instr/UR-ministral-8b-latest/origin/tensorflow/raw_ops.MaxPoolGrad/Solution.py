import tensorflow as tf

# Define the input tensors
x = tf.constant([[1.0, 2.0, 3.0],
                 [4.0, 5.0, 6.0]], dtype=tf.float32)

# Define the maxpooling operation
k = 3
max_pool_output = tf.raw_ops.MaxPoolingV2(
    input=x,
    ksize=[k, k],
    strides=[1, 1],
    padding='SAME')

# Define the function to compute gradients of the maxpooling function
def compute_gradients():
    with tf.GradientTape() as tape:
        tape.watch(max_pool_output)
        max_pool_output = max_pool_output.numpy()
    grads = tape.gradient(max_pool_output, x)
    return grads

# Compute the gradients
grads = compute_gradients()
print(grads)
