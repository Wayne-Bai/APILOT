import tensorflow as tf

def fractional_avg_pool_grad(orig_input_shape, out_backprop, row_seq, col_seq):
    # Calculate the gradient of the FractionalAvgPool operation
    return tf.raw_ops.FractionalAvgPoolGrad(orig_input=orig_input_shape,
                                            out_backprop=out_backprop,
                                            row_pooling_sequence=row_seq,
                                            col_pooling_sequence=col_seq,
                                            overlapping=True)
