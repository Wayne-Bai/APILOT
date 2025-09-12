import tensorflow as tf

def store_tensor(input_tensor):
    handle = tf.raw_ops.MutableDenseHashTableV2(
        empty_key=tf.constant([-1], dtype=tf.int64),
        deleted_key=tf.constant([-2], dtype=tf.int64),
        value_dtype=input_tensor.dtype,
        container="",
        shared_name="",
        use_node_name_sharing=True
    )
    key_tensor = tf.constant([0], dtype=tf.int64)  # Using a simple key to store the tensor
    value_tensor = tf.expand_dims(input_tensor, 0)  # Expand dims to match the insertion requirements
    insert_op = tf.raw_ops.MutableDenseHashTableV2Insert(
        table_handle=handle, 
        keys=key_tensor, 
        values=value_tensor
    )
    # Reading the stored tensor
    read_op = tf.raw_ops.MutableDenseHashTableV2Lookup(
        table_handle=handle, 
        keys=key_tensor, 
        default_value=tf.constant([0], dtype=input_tensor.dtype)
    )
    return handle, insert_op, read_op

# Sample usage:
with tf.compat.v1.Session() as sess:
    input_tensor = tf.constant([1, 2, 3, 4], dtype=tf.float32)
    handle, insert_op, read_op = store_tensor(input_tensor)
    sess.run(insert_op)  # Perform insert operation
    output_tensor = sess.run(read_op)  # Fetch the tensor
    print("Stored and Retrieved Tensor:", output_tensor)
