import tensorflow as tf

# Verify TensorFlow version
print(f"TensorFlow version: {tf.__version__}")

def create_tensor_of_ones(shape):
    return tf.ones(shape)

# Example usage
shape = (2, 3, 4)
tensor_of_ones = create_tensor_of_ones(shape)
print(tensor_of_ones)
