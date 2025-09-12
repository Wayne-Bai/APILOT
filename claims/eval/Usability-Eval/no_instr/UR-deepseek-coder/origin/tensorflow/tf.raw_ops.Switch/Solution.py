import tensorflow as tf

def _forward_data(data, pred):
    # Create a TensorFlow session
    with tf.compat.v1.Session() as sess:
        # Use tf.case to forward data based on the predicate
        output = tf.case(
            {tf.equal(pred, True): lambda: data},
            default=lambda: tf.constant(0.0),  # Default value if pred is False
            exclusive=True
        )
        # Run the session to get the output
        result = sess.run(output)
    return result

# Example usage
data = tf.constant(5.0)
pred = tf.constant(True)

result = _forward_data(data, pred)
print(result)  # Output: 5.0
