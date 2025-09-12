import tensorflow as tf

# Defining input tensor here
input_tensor = tf.keras.Input(shape=(5,), dtype=tf.int32)
input_tensor = tf.convert_to_tensor([[1, 2, 3, 4, 5],
                                     [1, 2, 0, 4, 5],
                                     [0, 1, 0, 4, 0],
                                     [0, 1, 0, 0, 0],
                                     [1, 2, 3, 4, 0]])

def bin_counting(input_tensor):
    # DBScan does not have count bin counts
    results = []
    for bin_index in range(5):
        # Count occurrences of bin_index
        occurrences = tf.reduce_sum(tf.cast(input_tensor == bin_index, dtype=tf.int32))
        results.append(occurrences)
    return results

result = bin_counting(input_tensor)
result.numpy()
