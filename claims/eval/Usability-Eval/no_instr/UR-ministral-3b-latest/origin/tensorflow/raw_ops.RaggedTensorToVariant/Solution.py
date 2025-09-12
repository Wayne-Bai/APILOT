import tensorflow as tf

def encode_ragged_tensor(ragged_tensor):
    return tf.raw_ops.EncodeRaggedToVariant(ragged_tensor)

ragged_tensor = tf.TensorSlice("abc\n1","def\n2\n3","g\n")
encoded_tensor = encode_ragged_tensor(ragged_tensor)

for i in range(encoded_tensor.shape[0]):
    print(encoded_tensor[i])

