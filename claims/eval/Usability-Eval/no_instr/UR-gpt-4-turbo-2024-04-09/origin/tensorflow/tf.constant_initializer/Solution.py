import tensorflow as tf

def create_constant_tensor(shape, value):
    return tf.constant(value, shape=shape, dtype=tf.float32)

# Example usage:
tensor = create_constant_tensor(shape=(3, 4), value=7.0)
print(tensor)
