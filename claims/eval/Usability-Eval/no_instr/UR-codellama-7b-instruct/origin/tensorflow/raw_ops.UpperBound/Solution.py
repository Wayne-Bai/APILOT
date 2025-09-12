
import tensorflow as tf

# Define a custom operation that applies upper_bound to each row of sorted_search_values and values
@tf.custom_gradient
def upper_bound_per_row(sorted_search_values, values):
    # Calculate the upper bound for each row using numpy's fancy indexing
    output = np.max([sorted_search_values[i][:j] for i in range(sorted_search_values.shape[0]) for j in range(sorted_search_values.shape[1])], axis=1)
    
    # Define the gradients as identity functions
    def upper_bound_per_row_grad(output, d_output):
        return tf.nest.pack_sequence_as(d_output, [tf.identity(d_output[0]) for _ in range(sorted_search_values.shape[1])]), None
    
    # Register the gradient function
    grad = tape.watch(upper_bound_per_row)
    tf.nest.map_structure(lambda v: v.gradient_function.add_tape(grad, upper_bound_per_row_grad), output)
    
    return output
