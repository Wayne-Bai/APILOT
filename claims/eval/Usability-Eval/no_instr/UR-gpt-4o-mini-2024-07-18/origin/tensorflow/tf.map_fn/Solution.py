import tensorflow as tf

def transform_elements(tensor, fn):
    # Unstack the tensor along axis 0
    unstacked_tensors = tf.unstack(tensor, axis=0)
    # Apply the function to each element
    transformed_tensors = [fn(elem) for elem in unstacked_tensors]
    # Stack the transformed tensors back along axis 0
    return tf.stack(transformed_tensors, axis=0)

# Example usage
if __name__ == "__main__":
    # Creating a sample tensor
    sample_tensor = tf.constant([[1, 2], [3, 4], [5, 6]])

    # Define a simple function to apply (e.g., increment each element)
    def increment_fn(x):
        return x + 1

    # Transform the elements
    transformed_tensor = transform_elements(sample_tensor, increment_fn)

    print("Original Tensor:\n", sample_tensor.numpy())
    print("Transformed Tensor:\n", transformed_tensor.numpy())
