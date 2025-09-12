import tensorflow as tf

# Define the input tensors
input_tensor = tf.constant([1, 2, 3, 4, 5])
pred_tensor = tf.constant([True, False, True, False, True])

# Define the output tensors
output_tensor1 = tf.constant([10, 20, 30])
output_tensor2 = tf.constant([40, 50, 60])

# Create the Case operation
output = tf.raw_ops.Case(
    pred=[pred_tensor],
    fn=[lambda: output_tensor1, lambda: output_tensor2]
)

# Print the output tensor
print(output)
