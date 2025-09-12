import tensorflow as tf

def sparse_apply_div(var, indices, values):
    """
    Divides sparse updates into the variable referenced by `resource`.

    This operation computes

    # Add sparse updates to the variable.
    var = var + sparse_delta

    Args:
      var: A `ResourceVariable` object.
      indices: A `Tensor` of type `int32` with shape `[d_0, ..., d_n)` where `n` is the
        number of dimensions of `var`, and `d_i` is the number of updates for each
        dimension, respectively.
      values: A `Tensor` of type `dtype` with shape `[d_0, ..., d_n)`. The values
        corresponding to the elements represented by `indices`.

    Returns:
      The updated variable.
    """
    return tf.raw_ops.VarHandleOp(var, indices, values, dtype=var.dtype, shape=var.shape)
