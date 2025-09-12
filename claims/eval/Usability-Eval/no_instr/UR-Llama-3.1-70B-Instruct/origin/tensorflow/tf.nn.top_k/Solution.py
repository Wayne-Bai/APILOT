# Importing the necessary libraries
import tensorflow as tf

# Function to find k largest entries for the last dimension
def k_largest_entries(tensor, k):
    """
    Finds values and indices of the k largest entries for the last dimension.

    Args:
    - tensor: Input tensor
    - k: Number of largest entries to find

    Returns:
    - values: Values of the k largest entries
    - indices: Indices of the k largest entries
    """
    # Find values and indices of the k largest entries
    values, indices = tf.nn.top_k(tensor, k)

    return values, indices

# Example usage:
if __name__ == "__main__":
    # Create a sample tensor
    tensor = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    # Find 2 largest entries for the last dimension
    k = 2
    values, indices = k_largest_entries(tensor, k)

    print("Input Tensor:")
    print(tensor)
    print(f"\n{k} Largest Entries (Values):")
    print(values)
    print(f"\n{k} Largest Entries (Indices):")
    print(indices)
