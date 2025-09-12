import tensorflow as tf

def store_tensor(input_tensor):
    """
    Store the input tensor in the state of the current session using TensorFlow's low-level ops.
    Returns a handle to the stored tensor.
    """
    return tf.raw_ops.MutableDenseHashTableV2(
        empty_key=tf.constant(-1, dtype=tf.int64),
        deleted_key=tf.constant(-2, dtype=tf.int64),
        value_dtype=input_tensor.dtype,
        value_shape=input_tensor.shape,
        initial_num_buckets=1,
        container="",
        shared_name=""
    ).insert(keys=tf.constant([0], dtype=tf.int64), values=tf.expand_dims(input_tensor, 0))
