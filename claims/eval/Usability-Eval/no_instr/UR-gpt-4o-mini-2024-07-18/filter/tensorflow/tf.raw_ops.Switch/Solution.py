import tensorflow as tf

@tf.function
def forward_data_based_on_pred(data, pred):
    """
    Forwards data to different output ports based on pred.
    
    Arguments:
    data -- the input tensor
    pred -- a boolean tensor, where True sends data to one output and False
            sends it to another output.
    
    Returns:
    output_true -- data forwarded if pred is True
    output_false -- data forwarded if pred is False
    """
    output_true = tf.identity(data) if pred else tf.zeros_like(data)
    output_false = tf.zeros_like(data) if pred else tf.identity(data)

    return output_true, output_false

# Example Usage
data = tf.constant([1.0, 2.0, 3.0])
pred = tf.constant(True)

output_true, output_false = forward_data_based_on_pred(data, pred)
print("Output True:", output_true.numpy())
print("Output False:", output_false.numpy())
