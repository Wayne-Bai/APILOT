
import tensorflow as tf

# Input data
sorted_search_values = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]
values = [1.0, 1.5, 2.0]

# Define a function to apply the upper bound operation
def apply_upper_bound(sorted_search_values, values):
    # Create a tensor for the output
    output = tf.TensorArray(dtype=tf.float32)

    # Iterate over each row in the input data
    for i in range(len(sorted_search_values)):
        # Get the current row and sort it
        sorted_row = sorted(sorted_search_values[i])

        # Apply the upper bound operation
        upper_bound_value = sorted_row[-1]

        # Add the result to the output tensor
        output = tf.concat([output, tf.fill([1], upper_bound_value)], 0)

    return output

# Apply the function to the input data
output = apply_upper_bound(sorted_search_values, values)
