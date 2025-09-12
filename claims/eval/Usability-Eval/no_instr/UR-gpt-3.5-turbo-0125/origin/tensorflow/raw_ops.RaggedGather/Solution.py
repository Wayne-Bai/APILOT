
import tensorflow as tf

def gather_ragged_slices(params, indices):
    # Create a RaggedTensor from params
    rt_params = tf.RaggedTensor.from_nested_row_splits(params, nested_row_splits=[params.row_splits])

    # Gather ragged slices from params along axis 0 according to indices
    output = tf.raw_ops.RaggedGather(
        params=rt_params,
        indices=indices
    )

    return output
