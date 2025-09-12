
import tensorflow as tf

# Define the input and output tensors
input_tensor = tf.constant([1, 2, 3], dtype=tf.int32)
output_tensor = tf.raw_ops.EncodeWideVocabulary(
    input=input_tensor,
    vocab_size=5,
    num_oov_buckets=1,
    bucket_width=4,
    output_type=tf.string
)

# Print the result
print(output_tensor.numpy())
