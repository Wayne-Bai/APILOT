import tensorflow as tf

def create_ngrams(ragged_data, n):
    # Convert ragged data to dense tensor
    dense_data = tf.reshape(ragged_data, (-1,))

    # Create n-grams using tf.raw_ops.Ngrams
    ngrams = tf.raw_ops.Ngrams(dense_data, n)

    return ngrams

# Example usage:
# Create some ragged data
ragged_data = tf.constant([[1, 2], [3, 4, 5], [6]])

# Create 2-grams
ngrams = create_ngrams(ragged_data, 2)

# Print the resulting n-grams
print(ngrams)
