import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

def distributed_sdca_optimizer(loss_op, global_step, learning_rate, num_workers, num_features):
    goal = tf.placeholder(tf.float32, shape=[num_features])

    with tf.device("/job:worker/task:0"):
        W = tf.Variable(tf.zeros(num_features))
        update_W = tf.assign(W, tf.clip_by_value(W + learning_rate * (goal - W), -1.0, 1.0))

    with tf.device("/job:worker"):
        # Calculate gradients and update variables for each worker
        update_ops = []
        for i in range(1, num_workers):
            with tf.device("/job:worker/task:" + str(i)):
                W_i = tf.Variable(tf.zeros(num_features))
                update_W_i = tf.assign(W_i, tf.clip_by_value(W_i + learning_rate * (goal - W_i), -1.0, 1.0))
                update_ops.append(update_W_i)

    return tf.group(*[tf.cond(tf.equal(tf.mod(global_step, tf.constant(num_workers, dtype=tf.int64)),
                                       tf.constant(i, dtype=tf.int64)), lambda: update_op, lambda: tf.no_op())
                     for i, update_op in enumerate([update_W] + update_ops)])
