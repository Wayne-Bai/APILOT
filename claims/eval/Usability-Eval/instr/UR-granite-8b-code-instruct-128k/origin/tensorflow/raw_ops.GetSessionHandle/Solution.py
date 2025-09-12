
import tensorflow as tf

def store_tensor_in_session_state(tensor):
    return tf.raw_ops.VarHandleOp(shape=tensor.shape, dtype=tensor.dtype)
