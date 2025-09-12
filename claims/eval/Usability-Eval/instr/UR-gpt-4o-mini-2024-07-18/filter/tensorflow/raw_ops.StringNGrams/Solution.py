import tensorflow as tf

def create_ngrams_from_ragged_strings(ragged_strings, n):
    # Convert ragged tensor to list of strings
    flattened_strings = ragged_strings.to_list()
    
    # Generate n-grams
    ngrams = []
    for strings in flattened_strings:
        for string in strings:
            for i in range(len(string) - n + 1):
                ngram = string[i:i+n]
                ngrams.append(ngram)
    
    return ngrams

# Example usage
ragged_strings = tf.ragged.constant([["hello", "world"], ["tensorflow", "is", "great"]])
n = 2
ngrams = create_ngrams_from_ragged_strings(ragged_strings, n)
print(ngrams)
