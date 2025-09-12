import tensorflow as tf

def constant_tensor(shape, value):
    return tf.constant(value, shape=shape)

# Example usage
tensor_shape = (3, 3)
constant_value = 5
tensor = constant_tensor(tensor_shape, constant_value)
print(tensor)
