import tensorflow as tf

@tf.function
def control_flow(pred, true_branch, false_branch):
    return tf.raw_ops.Switch(inputs=[true_branch, false_branch], pred=pred)

# Example usage
pred = tf.constant(True)  # Change to False to switch branches
true_branch_output = tf.constant("True branch")
false_branch_output = tf.constant("False branch")

output = control_flow(pred, true_branch_output, false_branch_output)

tf.print(output)  # Will print either "True branch" or "False branch" based on the predicate
