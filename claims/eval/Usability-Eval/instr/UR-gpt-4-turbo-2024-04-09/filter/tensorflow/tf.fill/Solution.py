import tensorflow as tf

def create_filled_tensor(shape, scalar_value):
    return tf.fill(shape, scalar_value)

# Example usage
tensor = create_filled_tensor([2, 3], 5.0)
print(tensor)
