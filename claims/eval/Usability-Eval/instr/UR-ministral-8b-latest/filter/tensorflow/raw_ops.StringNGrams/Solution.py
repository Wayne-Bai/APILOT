import tensorflow as tf

def create_ngrams(ragged_tensors):
    ngrams = []
    for ragged_tensor in ragged_tensors:
        for element in ragged_tensor.to_tensor().numpy().tolist():
            ngrams.append(tf.constant(element))
    return ngrams

# Example usage
ragged_strings = tf.raw_ops.RaggedTensor1d.from_field_value(
    tf.raw_ops.RaggedStrings(['hello', 'world', 'ai'], ['hello', 'world'], [[2, 0], [1, 0], []]))
ngrams = create_ngrams([ragged_strings])
print(ngrams)
