import tensorflow as tf

# Assuming input is a 4D tensor
input_tensor = tf.random.uniform([1, 100, 100, 3])

# Define a fractional max pooling operation with a pooling ratio of 2
fmp_layer = tf.keras.layers.FractionalMaxPooling2D(
    pool_size=(2, 2), strides=(2, 2), padding='VALID')

# Apply the fractional max pooling operation to the input tensor
output_tensor = fmp_layer(input_tensor)

# Print the shape of the output tensor
print(output_tensor.shape)
