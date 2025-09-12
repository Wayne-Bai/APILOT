
import tensorflow as tf

@tf.function
def reverse_slices(input_tensor, starts, limits):
    return tf.raw_ops.ReverseSequence(
        input=input_tensor,
        seq_lengths=limits - starts,
        seq_dim=0,
        batch_dim=1
    )

# Example usage
input_tensor = tf.constant([[1, 2, 3, 4], [5, 6, 7, 8]], dtype=tf.float32)
starts = tf.constant([1, 0], dtype=tf.int32)
limits = tf.constant([4, 2], dtype=tf.int32)

output = reverse_slices(input_tensor, starts, limits)
print(output)
