import tensorflow as tf

# Define the shape and dtype of the input tensor
shape = [10, 10]  # 2D matrix with 10 rows and 10 columns
dtype = tf.float32

# Generate a random input tensor
input_tensor = tf.random.normal(shape=shape, dtype=dtype)

# Apply the inverse real-valued fast Fourier transform to the input tensor
output = tf.raw_ops.InverseRealFFT(inputs=input_tensor)

# Print the output tensor
print(output)
