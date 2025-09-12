import tensorflow as tf

def _forward_data(data, pred):
    # Create a boolean tensor based on the predicate
    pred_bool = tf.cast(pred, tf.bool)
    
    # Use tf.where to select the output based on the predicate
    output = tf.where(pred_bool, data, tf.zeros_like(data))
    
    return output

# Example usage
data = tf.constant([1.0, 2.0, 3.0])
pred = tf.constant(1)  # Predicate that determines the output port

result = _forward_data(data, pred)
print(result.numpy())
