import tensorflow as tf

def gather_slices(resource, indices, validation_string=None):
    return tf.raw_ops.ResourceGather(resource, indices, validation_string=validation_string)

# Example usage
if __name__ == "__main__":
    with tf.Session() as sess:
        resource = tf.Variable(initial_value=[0.1, 0.2, 0.3, 0.4, 0.5], dtype=tf.float32)
        indices = tf.constant([1, 3], dtype=tf.int32)
        
        sess.run(tf.global_variables_initializer())
        
        result = gather_slices(resource.handle, indices)
        print(sess.run(result))
