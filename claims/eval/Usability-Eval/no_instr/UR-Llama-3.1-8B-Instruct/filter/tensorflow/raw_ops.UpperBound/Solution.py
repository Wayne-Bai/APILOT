# Import necessary libraries
import tensorflow as tf
from tensorflow.keras import backend as K

# Define a function to apply upper_bound along each row
def upper_bound(sorted_values, values):
    """
    Applies upper_bound along each row.

    Args:
        sorted_values (tf.Tensor): A 2D tensor of sorted values.
        values (tf.Tensor): A 2D tensor of values to find the upper bound for.

    Returns:
        tf.Tensor: A 2D tensor with the upper bound for each row.
    """

    # Define the upper_bound function
    def upper_bound_func(sorted_row, value):
        # Get the indices where the value is greater than the sorted row entries
        indices = tf.where(tf.greater(sorted_row, value))

        # If no indices are found, return the length of the sorted row
        if not tf.size(indices):
            return tf.shape(sorted_row)[0]

        # Get the last index (the first if equal, the last if smaller) to get the upper bound
        upper_bound_idx = tf.reduce_max(indices)

        # Get the value at the upper bound index
        return tf.gather(sorted_row, upper_bound_idx)

    # Apply upper_bound_func along each row
    return tf.map_fn(lambda x: upper_bound_func(x[0], x[1]), (sorted_values, values), fn_output_signature=tf.int32)

# Generate test data
sorted_values = tf.constant([[1, 3, 5, 7], [2, 4, 6, 8], [0, 10, 20, 30]])
values = tf.constant([[2, 3, 5], [5, 6, 7], [9, 11, 15]])

# Call the upper_bound function
result = upper_bound(sorted_values, values)

print(result)
