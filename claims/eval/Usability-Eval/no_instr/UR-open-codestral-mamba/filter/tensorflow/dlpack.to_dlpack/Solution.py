import tensorflow as tf

# Assuming we have a tensor 't'
t = tf.constant([1.0, 2.0, 3.0], dtype=tf.float32)

# This will return the dlpack capsule representing the tensor 't'
dlpack_capsule = t._datatype_ptr_repr
print(dlpack_capsule)
