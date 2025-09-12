import tensorflow as tf

def gather_slices(resource, indices):
    return tf.gather(resource, indices)

# Example usage
if __name__ == "__main__":
    # Create a tensor variable
    resource_tensor = tf.Variable([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=tf.int32)
    
    # Indices for gathering
    indices = tf.constant([0, 2])  # Gather the 0th and 2nd slices

    # Call the gather_slices function
    gathered_slices = gather_slices(resource_tensor, indices)

    print(gathered_slices.numpy())  # Output the gathered slices
