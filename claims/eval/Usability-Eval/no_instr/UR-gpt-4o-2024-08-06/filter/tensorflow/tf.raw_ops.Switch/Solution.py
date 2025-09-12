import tensorflow as tf

def dynamic_switch(data, pred):
    """
    Forwards data to the output port determined by the predicate pred.
    Mimics the functionality typically handled by `tf.raw_ops.Switch`.

    :param data: Tensor which needs to be forwarded.
    :param pred: Boolean tensor which determines which output the data should be sent to.
                 If pred is true, data is sent to true_path; otherwise, to false_path.
    :return: Two tensors, one for the true path and another for the false path.
    """
    # Using tf.where to implement the switch functionality
    true_path = tf.where(pred, data, tf.zeros_like(data))
    false_path = tf.where(pred, tf.zeros_like(data), data)

    return true_path, false_path

# Example Usage:
# Define a tensor
data_tensor = tf.constant([1, 2, 3, 4, 5])

# Define a predicate tensor
predicate_tensor = tf.constant([True, False, True, False, True])

# Call the dynamic_switch function
true_output, false_output = dynamic_switch(data_tensor, predicate_tensor)

# Print the results
print("True Path Output:", true_output.numpy())
print("False Path Output:", false_output.numpy())
