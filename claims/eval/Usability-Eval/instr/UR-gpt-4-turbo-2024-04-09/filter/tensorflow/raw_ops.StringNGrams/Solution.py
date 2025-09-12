import tensorflow as tf

def create_ngrams(data, n):
    # Create a RaggedTensor from string data
    ragged_data = tf.ragged.constant(data)
    # Compute the ngrams
    ngrams = tf.strings.ngrams(ragged_data, n, separator='')
    return ngrams

# Example data
data = [['one', 'two', 'three'], ['four', 'five', 'six', 'seven']]
n = 2

# Create ngrams
result = create_ngrams(data, n)
print(result)
