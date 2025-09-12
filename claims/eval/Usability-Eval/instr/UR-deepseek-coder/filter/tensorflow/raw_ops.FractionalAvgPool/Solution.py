import tensorflow as tf

def fractional_avg_pool(input_tensor, pooling_ratio, pseudo_random=False, overlapping=False, seed=0, seed2=0):
    # Calculate the target output sizes
    input_shape = tf.shape(input_tensor)
    output_shape = [tf.cast(tf.math.ceil(input_shape[i] / pooling_ratio[i]), tf.int32) for i in range(input_tensor.shape.ndims)]

    # Generate pooling sequence
    def generate_pooling_sequence(input_size, output_size, seed):
        random_state = tf.random.experimental.stateless_uniform([input_size], seed=[seed, seed + 1], minval=0, maxval=1)
        sorted_indices = tf.argsort(random_state)
        return tf.gather(sorted_indices, tf.range(output_size))

    pooling_sequences = [generate_pooling_sequence(input_shape[i], output_shape[i], seed + i) for i in range(input_tensor.shape.ndims)]

    # Perform pooling
    def pool_fn(input_slice, pooling_sequence):
        return tf.reduce_mean(tf.gather(input_slice, pooling_sequence), axis=0)

    pooled_output = tf.map_fn(lambda x: pool_fn(x, pooling_sequences[1]), input_tensor, dtype=tf.float32)
    pooled_output = tf.map_fn(lambda x: pool_fn(x, pooling_sequences[0]), pooled_output, dtype=tf.float32)

    return pooled_output, pooling_sequences

# Example usage:
input_tensor = tf.random.normal([1, 224, 224, 3])
pooling_ratio = [1.0, 1.5, 1.5, 1.0]
output_tensor, pooling_sequences = fractional_avg_pool(input_tensor, pooling_ratio)
print(output_tensor)
