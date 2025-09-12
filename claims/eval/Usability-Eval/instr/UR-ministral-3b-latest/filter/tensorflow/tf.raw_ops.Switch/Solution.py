import tensorflow as tf

def my_method(pred):
    input = tf.raw_ops.MyRawOp(
        input_tensors=[tf.random.uniform([100, 100])], # Example input tensor
        pred=pred
    )
    return input
