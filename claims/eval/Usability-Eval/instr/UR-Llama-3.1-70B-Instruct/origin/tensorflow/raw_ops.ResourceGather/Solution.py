# Import necessary libraries
import tensorflow as tf

# Define the Gather op
def gather_slices(resource, indices, validation_STRING=""):
    """
    Gather slices from the variable pointed to by resource according to indices.

    Args:
    resource (tf.Tensor): The variable to gather slices from.
    indices (tf.Tensor): The indices of the slices to gather.
    validation_STRING (str, optional): The validation string. Defaults to "".

    Returns:
    tf.Tensor: The gathered slices.
    """
    return tf.raw_ops.GatherV2(
        resource=resource,
        indices=indices,
        axis=0,  # Default axis is 0
        batch_dims=0,  # Default batch dimensions is 0
        name="gather_slices"
    )

# Example usage
if __name__ == "__main__":
    # Create a resource tensor
    resource = tf.constant(
        values=[[1, 2], [3, 4], [5, 6]],
        dtype=tf.int32
    )

    # Create indices tensor
    indices = tf.constant(
        values=[1, 2],
        dtype=tf.int32
    )

    # Gather slices
    gathered_slices = gather_slices(resource, indices)

    # Print the gathered slices
    with tf.Session() as sess:
        print(sess.run(gathered_slices))
