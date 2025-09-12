import tensorflow as tf

# Function to perform sparse-output bin counting for a sparse tensor input
def sparse_bin_count(sparse_tensor, num_bins, bin_edges):
    # Ensure the input is a SparseTensor
    if not isinstance(sparse_tensor, tf.SparseTensor):
        raise ValueError("Input must be a SparseTensor.")
    
    # Get the values from the sparse tensor
    values = sparse_tensor.values
    
    # Create a histogram based on the values, bin edges, and number of bins
    histogram, _ = tf.histogram_fixed_width(values, bin_edges, nbins=num_bins)
    
    return histogram

# Example usage
# Creating a sparse tensor
indices = [[0, 0], [1, 2], [2, 1]]
values = [1, 2, 3]
dense_shape = [3, 3]
sparse_tensor = tf.SparseTensor(indices=indices, values=values, dense_shape=dense_shape)

# Define bin edges and number of bins
bin_edges = [0, 1, 2, 3, 4]
num_bins = len(bin_edges) - 1

# Call the function to perform sparse-output bin counting
histogram = sparse_bin_count(sparse_tensor, num_bins, bin_edges)

# Print the histogram results
print(histogram.numpy())
