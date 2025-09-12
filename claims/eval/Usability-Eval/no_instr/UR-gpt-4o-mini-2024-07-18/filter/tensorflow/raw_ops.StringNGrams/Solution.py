import tensorflow as tf

def create_ngrams(ragged_strings, n):
    # Convert ragged strings to ngrams
    # Create a RaggedTensor from ragged_strings
    ragged_tensor = tf.ragged.constant(ragged_strings)

    # Function to compute n-grams
    def ngram_func(strings):
        ngrams = []
        for string in strings:
            # Create n-grams for each string
            string_ngrams = [string[i:i+n] for i in range(len(string) - n + 1)]
            ngrams.append(string_ngrams)
        return ngrams

    # Map the ngram function over the ragged tensor
    return ragged_tensor.flat_values.map(ngram_func)

# Example usage
ragged_strings = [['hello', 'world'], ['tensorflow', 'rocks']]
n = 2
ngrams_result = create_ngrams(ragged_strings, n)
print(ngrams_result)
