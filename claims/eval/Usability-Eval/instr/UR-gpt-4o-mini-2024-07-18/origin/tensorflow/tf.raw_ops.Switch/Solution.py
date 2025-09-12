import tensorflow as tf

@tf.function
def forward_data(pred, data):
    # Create a tf.raw_ops.switch_case operation
    output = tf.raw_ops.SwitchCase(
        branch_indices=pred,
        operands=[data],
        uniform_condition=False
    )
    return output

# Example usage
pred = tf.constant([0, 1, 2])  # Example predicate
data = tf.constant([10, 20, 30])  # Example data

result = forward_data(pred, data)
print(result)
