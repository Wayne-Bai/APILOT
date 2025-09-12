import tensorflow as tf

def segment_sum(data, segment_ids):
    segment_ids = tf.convert_to_tensor(segment_ids)
    data = tf.convert_to_tensor(data)

    # Get the unique segment ids
    unique_ids, _ = tf.unique(segment_ids)

    # Create an array to hold the segment sums
    num_segments = tf.shape(unique_ids)[0]
    segment_sums = tf.TensorArray(data.dtype, size=num_segments, dynamic_size=False)

    # Initialize each segment sum to 0
    for i in tf.range(num_segments):
        segment_sums = segment_sums.write(i, 0)

    # For each data point, add it to the corresponding segment sum
    for i in tf.range(tf.shape(data)[0]):
        segment_id = segment_ids[i]
        segment_index = tf.where(tf.equal(unique_ids, segment_id))[0, 0]
        segment_sums = segment_sums.write(segment_index, segment_sums.read(segment_index) + data[i])

    # Convert the TensorArray to a tensor
    segment_sums = segment_sums.stack()

    return segment_sums

# Test the function
data = tf.constant([1, 2, 3, 4, 5, 6], dtype=tf.int32)
segment_ids = tf.constant([0, 0, 1, 1, 2, 2], dtype=tf.int32)
print(segment_sum(data, segment_ids))
