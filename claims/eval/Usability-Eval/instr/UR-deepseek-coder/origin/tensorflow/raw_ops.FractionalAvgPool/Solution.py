import tensorflow as tf

def fractional_avg_pool(value, pooling_ratio, pseudo_random=False, overlapping=False, seed=0, seed2=0):
    # Calculate the target output sizes
    input_shape = tf.shape(value)
    output_shape = [tf.cast(tf.math.ceil(input_shape[i] / pooling_ratio[i]), tf.int32) for i in range(value.shape.ndims)]

    # Generate the pooling sequence
    row_seq = tf.cast(tf.linspace(0.0, tf.cast(input_shape[1] - 1, tf.float32), output_shape[1] + 1), tf.int32)
    col_seq = tf.cast(tf.linspace(0.0, tf.cast(input_shape[2] - 1, tf.float32), output_shape[2] + 1), tf.int32)

    # Perform the pooling
    pooled = tf.image.extract_patches(
        value[tf.newaxis, ...],
        sizes=[1, row_seq[1] - row_seq[0], col_seq[1] - col_seq[0], 1],
        strides=[1, row_seq[1] - row_seq[0], col_seq[1] - col_seq[0], 1],
        rates=[1, 1, 1, 1],
        padding='VALID'
    )

    # Average the patches
    pooled = tf.reduce_mean(pooled, axis=[1, 2])

    return pooled, row_seq, col_seq

# Example usage
input_tensor = tf.random.normal([1, 224, 224, 3])
pooling_ratio = [1.0, 1.5, 1.5, 1.0]
output_tensor, row_seq, col_seq = fractional_avg_pool(input_tensor, pooling_ratio)
