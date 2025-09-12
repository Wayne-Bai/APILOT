import tensorflow as tf

def serialize_tensor(tensor):
    return tf.io.serialize_tensor(tensor)

# Example usage
if __name__ == "__main__":
    tensor = tf.constant([[1, 2], [3, 4]])
    serialized_tensor = serialize_tensor(tensor)
    print(serialized_tensor)
