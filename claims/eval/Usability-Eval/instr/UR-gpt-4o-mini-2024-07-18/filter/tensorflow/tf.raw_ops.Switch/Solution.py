import tensorflow as tf

@tf.function
def forward_based_on_pred(pred, data):
    output = tf.raw_ops.Switch(data=data, pred=pred)
    return output

# Example usage
# pred = tf.constant(True)  # This determines which output to use
# data = tf.constant([1.0, 2.0, 3.0])
# output_data = forward_based_on_pred(pred, data)
# print(output_data)
