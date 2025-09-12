
import tensorflow as tf

@tf.function
def compute_convolution_gradients(input_tensor, filter):
    with tf.GradientTape() as tape:
        tape.watch(input_tensor)
        output = tf.nn.conv2d(input_tensor, filter, strides=[1, 1, 1, 1], padding='SAME')
    gradients = tape.gradient(output, input_tensor)
    
    return gradients

# Example usage
input_tensor = tf.random.normal((1, 28, 28, 3))
filter = tf.random.normal((3, 3, 3, 64))
gradients = compute_convolution_gradients(input_tensor, filter)
print(gradients)
