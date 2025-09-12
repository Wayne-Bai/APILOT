import tensorflow as tf

def serialize_initializer(init):
    """
    Serialize a TensorFlow initializer into a string representation.

    Args:
    init: TensorFlow initializer object.

    Returns:
    str: Serialized string representation of the initializer.
    """
    return init.to_json()

def deserialize_initializer(serialized_init):
    """
    Deserialize a TensorFlow initializer from a string representation.

    Args:
    serialized_init: String representation of the TensorFlow initializer.

    Returns:
    tf.keras.initializers.Initializer: Deserialized TensorFlow initializer object.
    """
    init_dict = tf.compat.v1.decode_json(serialized_init)
    initializer_class = getattr(tf.keras.initializers, init_dict['class'])
    return initializer_class(**init_dict['config'])

# Example usage:
my_init = tf.keras.initializers.RandomNormal(mean=0.0, stddev=1.0)
serialized = serialize_initializer(my_init)
deserialized = deserialize_initializer(serialized)
print(deserialized)
