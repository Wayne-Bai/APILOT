import tensorflow as tf

def levenshtein_distance(y_true, y_pred):
    d = tf.cast(tf.shape(y_true)[-1], tf.float32)
    y_true = tf.cast(y_true, tf.int32)
    y_pred = tf.cast(y_pred, tf.int32)

    indices = tf.where(tf.math.not_equal(y_true, y_pred))
    x = tf.gather_nd(y_true, indices)
    y = tf.gather_nd(y_pred, indices)

    len_x = tf.shape(x)[0]
    len_y = tf.shape(y)[0]
    b = tf.fill([len_x + len_y,], tf.cast(tf.minimum(len_x, len_y), dtype=tf.int32))
    indices = tf.cast(indices[:, -1], tf.int32)
    updates = indices + b
    dense_shape = [len_x + len_y, tf.shape(y_true)[-1]]
    ids = tf.scatter_nd(tf.stack([tf.range(len_x + len_y), indices], axis=-1), updates, dense_shape)

    band = tf.cast(tf.maximum(len_x - len_y, len_y - len_x), tf.int32)
    lev = tf.expand_dims(tf.range(tf.maximum(len_x, len_y) + 1), axis=-1)
    lev = tf.cast(tf.tile(lev, [1, tf.shape(y_true)[-1]]), tf.int32)
    diag_mask = tf.cast(tf.equal(ids[:, :-1] + 1, ids[:, 1:]), tf.int32)
    diag_mask = tf.concat([tf.ones([tf.shape(y_true)[-1]], dtype=tf.int32), diag_mask[0, :]], 0)
    lev += tf.cumsum((1 - diag_mask[:, None]), axis=0)
    lev = tf.RaggedTensor.from_tensor(lev, lengths=(len_x + len_y + 1))

    mask = tf.sequence_mask(tf.shape(y_true)[-1], tf.shape(y_true)[-1])
    band = tf.expand_dims(tf.range(-band, band + 1), axis=-1)
    band = tf.tile(band, [1, tf.shape(y_true)[-1]])
    band = tf.cast(tf.RaggedTensor.from_tensor(band, lengths=2*band[0, :] + 1), tf.int32)
    indices = tf.cumsum(tf.ones_like(ids[:, :-1]), exclusive=True, axis=-1)
    indices = tf.expand_dims(indices, axis=-1)
    lev_sim = tf.where(mask, tf.abs(band - indices), tf.zeros_like(band)) + tf.cast( lev, band.dtype)
    lev_sim = tf.where(band >= tf.expand_dims(-lev[:, 1:] + lev[:, :-1], 1), lev_sim, tf.ones_like(lev_sim)*tf.cast(tf.reduce_max(lev_sim), tf.int32))
    lev_sim = tf.transpose(lev_sim, perm=[0, 2, 1])
    distance = tf.reduce_min(tf.cast(lev_sim[:, :-1, :], tf.float32), axis=-1)
    distance = distance[-1, :]

    return tf.math.divide_no_nan(distance, d)
