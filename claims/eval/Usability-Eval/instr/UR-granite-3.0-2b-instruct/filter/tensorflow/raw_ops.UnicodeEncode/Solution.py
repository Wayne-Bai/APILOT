import tensorflow as tf

# Define the input tensor
input_tensor = tf.constant([65, 66, 67])

# Define the Encode a tensor of ints into unicode strings operation
encode_op = tf.raw_ops.Encode(
    input=input_tensor,
    output_type=tf.string,
    output_shape=None,
    name=None
)

# Run the operation to get the output tensor
output_tensor = encode_op.run()

# Print the output tensor
print(output_tensor)
