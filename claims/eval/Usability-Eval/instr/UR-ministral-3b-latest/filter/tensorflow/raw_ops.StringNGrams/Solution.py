import tensorflow as tf

def create_ngrams(texts, n):
    # Convert texts to padded strings
    texts = tf.strings.pad(texts, [[0, 0]], side=tf.strings.PAD)
    # Create ngrams
    texts = tf.stringsgrams(texts, n)
    return texts

# Example usage:
texts = ["hello world", "goodbye world", "tensorflow operates with standard machine learning frameworks"]
ngrams = create_ngrams(texts, 2)
print(ngrams)
