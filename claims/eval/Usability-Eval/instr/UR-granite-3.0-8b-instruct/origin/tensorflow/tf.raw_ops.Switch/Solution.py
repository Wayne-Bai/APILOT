import tensorflow as tf

def forward_data(pred, data):
    output_port = tf.raw_ops.Switch(pred, data[0], data[1])
    return output_port
