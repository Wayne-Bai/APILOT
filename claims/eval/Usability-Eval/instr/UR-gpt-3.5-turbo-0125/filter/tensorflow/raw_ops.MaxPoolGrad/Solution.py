
import tensorflow as tf

@tf.RegisterGradient("MaxPool")
def _MaxPoolGrad(op, grad):
    return tf.raw_ops.MaxPoolGrad(op.inputs[0], grad, op.outputs[0], ksize=op.get_attr("ksize"), strides=op.get_attr("strides"), padding=op.get_attr("padding"))
