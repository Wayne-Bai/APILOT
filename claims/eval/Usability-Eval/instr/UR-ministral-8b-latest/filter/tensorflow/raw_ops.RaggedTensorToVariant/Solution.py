import tensorflow as tf

# Example usage of `tf.raw_operations.tf.EncodeV2`
x = tf.raw_ops.EncodeV2(
    input=tf.RaggedTensor.from_row_splits(
        values=[1, 2, 3, 4],
        row_splits=[0, 2, 3, 5]
    ),
    outer_lengths=None,
    batch_density=False,
    validate_shape=True
)
print(x)
