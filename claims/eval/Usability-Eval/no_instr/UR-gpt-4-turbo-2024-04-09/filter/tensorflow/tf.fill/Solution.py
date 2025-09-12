import tensorflow as tf

def create_filled_tensor(shape, value):
    return tf.fill(shape, value)

# Example usage:
tensor = create_filled_tensor([2, 3], 7)
print(tensor)
