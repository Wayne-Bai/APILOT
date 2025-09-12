import tensorflow as tf

# Create a RaggedTensor
values = tf.ragged.constant([[1, 2], [3, 4, 5], []], ragged_rank=1)

# Convert RaggedTensor to variant
rt_variant = tf.raw_ops.RaggedTensorToVariant(
    input_rt=values,
    out_type_spec=tf.Variant(tf.int32, shape=[tf.Dimension(None), tf.Dimension(None)]),
    encoding="ROW_SPLITS")

# Print the variant tensor
print(rt_variant)
