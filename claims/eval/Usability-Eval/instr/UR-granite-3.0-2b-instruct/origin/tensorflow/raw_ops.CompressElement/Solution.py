import tensorflow as tf

# Define the input dataset
input_dataset = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Define the compression method (e.g., quantization)
compression_method = "Quantization"

# Check if the compression method is supported
if compression_method in tf.raw_ops.COMPRESSION_METHODS:
    # Create a compression operation
    compression_op = tf.raw_ops.Compression(
        input=input_dataset,
        method=compression_method,
        level=0.5,  # Adjust the level as needed
        axis=-1,  # Compress along the last dimension
    )

    # Run the compression operation
    compressed_dataset = compression_op.execute()

    # Print the compressed dataset
    print("Compressed Dataset:")
    print(compressed_dataset)
else:
    print(f"Unsupported compression method: {compression_method}")
