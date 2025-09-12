import tensorflow as tf

def custom_api():
    # Start code with importing tensorflow
    data = tf.constant([1, 2, 3, 4, 5])
    pred = tf.constant([True, False, True, False, True])
    output = tf.raw_ops.Switch(data=data, pred=pred)
    return output
