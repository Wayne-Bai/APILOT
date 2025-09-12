import tensorflow as tf

def gather_slices(variable, indices):
    # Use tf.gather to gather slices from the variable based on indices
    return tf.gather(variable, indices)

# Example usage:
if __name__ == "__main__":
    # Create a sample variable
    variable = tf.Variable([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=tf.int32)

    # Define indices to gather
    indices = tf.constant([0, 2])

    # Gather slices
    gathered_slices = gather_slices(variable, indices)

    print(gathered_slices.numpy())
