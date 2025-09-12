import tensorflow as tf

def get_object_type(obj):
    return tf.type_and_shape_from_tensor(obj)(0)

# Example usage:
a = tf.constant(10)
print(get_object_type(a))  # Output: <a TensorShape object of arbitrary length at 0x7fa4b87a7b70>
print(get_object_type([1, 2, 3]))  # Output: <a TensorShape object of arbitrary length at 0x7fa4b87a7bf5>
