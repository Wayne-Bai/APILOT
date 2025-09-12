import tensorflow as tp

# Define the input tensor
input_tensor = tp.constant([1.0, 2.0, 3.0, 4.0, 5.0])

# Define the compression parameters
compression = tp.raw_ops.Compress(input=input_tensor, shape=[2, 2])

# Print the compressed tensor
print(compression)
