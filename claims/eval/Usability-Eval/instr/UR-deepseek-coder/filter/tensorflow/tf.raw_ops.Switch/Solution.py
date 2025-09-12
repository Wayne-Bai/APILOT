import tensorflow as tf

def _forward_data(data, pred):
    # Create a TensorFlow session
    with tf.compat.v1.Session() as sess:
        # Use tf.case to forward data based on the predicate
        result = tf.case(
            {tf.equal(pred, True): lambda: data},
            default=lambda: tf.zeros_like(data),
            exclusive=True
        )
        # Run the session to get the result
        return sess.run(result)

# Example usage
data = tf.constant([1, 2, 3])
pred = tf.constant(True)
output = _forward_data(data, pred)
print(output)
