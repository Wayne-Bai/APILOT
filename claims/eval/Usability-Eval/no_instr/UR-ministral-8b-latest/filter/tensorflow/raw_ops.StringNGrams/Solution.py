import tensorflow as tf

def create_ngrams(data, n):
    # Convert the string data to a ragged tensor
    ragged_data = tf.raw_ops.RaggedStringCheck("[", data)

    # Create ngrams using tf.raw_ops.RaggedSplitV2
    ngrams = tf.raw_ops.RaggedSplitV2(ragged=ragged_data, max_length=n)
    return ngrams

# Example usage
data = ["I love TensorFlow", "Deep learning is cool"]
ngrams = create_ngrams(data, 2)

for sentence in ngrams:
    for token in tf.raw_ops.RaggedSplitV2(sentence):
        print(token)
