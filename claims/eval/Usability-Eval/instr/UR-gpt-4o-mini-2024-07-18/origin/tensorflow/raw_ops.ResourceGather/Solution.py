import tensorflow as tf

# Define a function to gather slices from a variable using indices
def gather_slices(variable, indices):
    return tf.gather(variable, indices)

# Example usage
if __name__ == "__main__":
    # Create a sample variable
    variable = tf.Variable([[1, 2], [3, 4], [5, 6]], dtype=tf.int32)

    # Define the indices for gathering
    indices = tf.constant([0, 2])  # Gather the first and third slices

    # Gather slices
    result = gather_slices(variable, indices)

    # Print the result
    tf.print(result)
