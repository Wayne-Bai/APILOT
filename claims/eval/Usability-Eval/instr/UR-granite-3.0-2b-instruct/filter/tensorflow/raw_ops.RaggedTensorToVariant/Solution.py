import tensorflow as tf

def encode_ragged_to_variant(ragged_tensor):
    # Create a RaggedTensor to VariantConverter
    ragged_to_variant = tf.raw_ops.RaggedToVariant(
        ragged_tensor=ragged_tensor,
        variant_type=tf.string,  # Replace with the desired variant type
        name="encode_ragged_to_variant"
    )

    return ragged_to_variant
