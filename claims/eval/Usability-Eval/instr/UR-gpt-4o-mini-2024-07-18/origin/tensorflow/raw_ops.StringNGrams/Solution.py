import tensorflow as tf

def create_ngrams(ragged_strings, n):
    # Convert the ragged tensor to a regular tensor of strings
    ragged_tensor = tf.ragged.constant(ragged_strings)

    # Create ngrams using list comprehension
    ngrams = ragged_tensor.map_flat_values(lambda x: [x[i:i + n] for i in range(len(x) - n + 1)])

    return ngrams

# Example usage
ragged_strings = [["this", "is", "an", "example"], ["create", "ngrams", "from", "ragged", "data"]]
n = 2
ngrams_result = create_ngrams(ragged_strings, n)
print(ngrams_result)
