import tensorflow as tf

@tf.function
def maxpooling_with_gradients(input_tensor, pool_size, strides):
    # Create the max pooling layer
    pool_layer = tf.keras.layers.MaxPool2D(pool_size=pool_size, strides=strides)
    pooled_output = pool_layer(input_tensor)

    # Compute gradients
    with tf.GradientTape() as tape:
        tape.watch(input_tensor)
        pooled_output = pool_layer(input_tensor)

    # Get gradients
    gradients = tape.gradient(pooled_output, input_tensor)
    return pooled_output, gradients

# Example usage
input_tensor = tf.random.normal([1, 4, 4, 1])  # Batch size of 1, 4x4 images with 1 channel
pool_size = (2, 2)
strides = 2

pooled_output, gradients = maxpooling_with_gradients(input_tensor, pool_size, strides)
print("Pooled Output:\n", pooled_output.numpy())
print("Gradients:\n", gradients.numpy())
