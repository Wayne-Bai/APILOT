# Import necessary libraries
import tensorflow as tf

# Define a function that uses Gather
def gather_slices(resource, indices, validate_indices=True, axis=0):
    # Create a raw operation and return the output
    output = tf.raw_ops.GatherV2(
        params=resource,
        indices=indices,
        validate_indices=validate_indices,
        axis=axis
    )
    
    return output

# Example usage
if __name__ == "__main__":
    # Define a resource (2D Tensor)
    resource = tf.constant([[1, 2, 3], [4, 5, 6]])

    # Define indices for Gather
    indices = tf.constant([0, 1], dtype=tf.int32)

    # Gather slices from the resource
    output = gather_slices(resource, indices)

    # Print the output
    print("Output:", output.numpy())
