# Import the necessary library
import tensorflow as tf

# Create a sample input tensor
input_tensor = tf.constant([
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],  # First batch
    [[10, 11, 12], [13, 14, 15], [16, 17, 18]]
], dtype=tf.float32)

def fractional_average_pooling(input_tensor, pool_size, strides, padding):
    # Calculate the fractional pooling size
    frac_pool_size = tf.cast(pool_size * tf.image.extract_image_patches(
        tf.ones_like(input_tensor[:, :, None, :]),
        ksizes=[1, 1, pool_size, 1],
        strides=[1, 1, strides, 1],
        rates=[1, 1, 1, 1],
        padding=padding.upper()
    ), dtype=tf.float32)

    # fractional_pool_size is now the 3D tensor [[x, y], [x, y],...] with the fractional pooling coordinates in each pair.
    # Next, we compute the row-wise and column-wise indices using frac_pool_size.
    row_indices = tf.math.floor(frac_pool_size / strides)
    col_indices = tf.math.floor(frac_pool_size % strides)

    # We will use tf.gather to get the values that correspond to each index. To do this, we need to shape frac_pool_size,
    # row_indices, and col_indices to match the broadcasted dimensions of input_tensor.
    frac_pool_size = tf.expand_dims(frac_pool_size[..., 0], axis=-1)
    row_indices = tf.expand_dims(row_indices, axis=-1)
    col_indices = tf.expand_dims(col_indices, axis=-1)

    result = tf.gather(input_tensor,
                       [
                           tf.range(tf.shape(row_indices)[0]),
                           tf.math.cast(row_indices, dtype=tf.int64),
                           tf.math.cast(col_indices, dtype=tf.int64)
                       ],
                       axis=[1, 2]
                       )
    return tf.reduce_mean(result, axis=[1, 2])

# Test the function
print(fractional_average_pooling(input_tensor, pool_size=2, strides=2, padding='SAME'))
