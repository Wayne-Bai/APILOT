import tensorflow as tf

# Define a custom op that applies upper_bound along each row
class ApplyUpperBoundOp(tf.raw_op.RawOp):
    def __init__(self, sorted_search_values, values):
        super().__init__("ApplyUpperBound")
        self.sorted_search_values = sorted_search_values
        self.values = values

    def compute(self, session):
        # Get the input shapes
        sorted_search_values_shape = self.sorted_search_values.shape
        values_shape = self.values.shape

        # Check if the input shapes match
        if sorted_search_values_shape[1] != values_shape[0]:
            raise ValueError("The number of rows in sorted_search_values and values must match.")

        # Compute the upper bound along each row
        upper_bound = tf.maximum(sorted_search_values, self.values)

        # Return the result
        return tf.raw_operation(upper_bound)

# Create the op
sorted_search_values = tf.constant([[1, 2], [3, 4], [5, 6]], dtype=tf.float32)
values = tf.constant([[7, 8], [9, 10], [11, 12]], dtype=tf.float32)
op = ApplyUpperBoundOp(sorted_search_values, values)

# Run the op
with tf.Session() as sess:
    result = sess.run(op)
    print(result)
