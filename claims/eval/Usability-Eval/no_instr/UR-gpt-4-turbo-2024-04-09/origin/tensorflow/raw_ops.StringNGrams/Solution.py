import tensorflow as tf

def create_ngrams(data, n):
    # Create a RaggedTensor from string data
    rt = tf.ragged.constant(data, dtype=tf.string)

    # Use the `ngrams` operation available in TensorFlow
    ngrams = tf.strings.ngrams(rt, n)
    return ngrams

# Example data
string_data = [["hello", "world"], ["tensorflow", "is", "great"]]
n = 2

# Generate ngrams
result = create_ngrams(string_data, n)
print("Ngrams:", result)
