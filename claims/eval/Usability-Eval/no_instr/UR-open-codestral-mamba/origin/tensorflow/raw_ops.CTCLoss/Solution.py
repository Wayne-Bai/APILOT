import tensorflow as tf

def ctc_loss(y_true, y_pred, input_length, label_length):
    '''
    y_true: labels for the training data.
    y_pred: model's prediction.
    input_length: the length of model's input.
    label_length: the length of model's label.
    '''
    y_true = tf.cast(tf.nn.ctc_unique_labels(y_true, dtype=tf.int32), tf.int64)
    loss = tf.nn.ctc_loss(labels=y_true, inputs=y_pred, sequence_length=input_length, label_length=label_length)
    return tf.reduce_mean(loss)

# example usage:
input_length = [100]  # the length of model's input
label_length = [10]  # the length of model's label
y_true = tf.random.uniform((10,), dtype=tf.int32)  # random label
y_pred = tf.random.uniform((1, 100, 10), dtype=tf.float32)  # random prediction
loss = ctc_loss(y_true, y_pred, input_length, label_length)
print('loss:', loss.numpy())
