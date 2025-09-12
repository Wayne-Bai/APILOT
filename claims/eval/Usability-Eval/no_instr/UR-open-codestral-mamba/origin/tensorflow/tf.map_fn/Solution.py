import tensorflow as tf

def apply_fn_to_elements(tensor):
    return tf.map_fn(lambda x: x * 2, tensor, dtype=tf.float32)

tensor = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0], dtype=tf.float32)
result = apply_fn_to_elements(tensor)
print(result)
