import tensorflow as tf

def serialize_initializer(initializer):
    """
    Serialize a Keras initializer instance.
    :param initializer: The Keras initializer instance to serialize.
    :return: A serialized string representing the initializer.
    """
    return initializer.to_json()

def deserialize_initializer(serialized_init):
    """
    Deserialize a Keras initializer instance from a serialized string.
    :param serialized_init: The serialized string representing the initializer.
    :return: A Keras initializer instance.
    """
    initializer = tf.keras.initializers.from_json(serialized_init)
    return initializer

# Example usage:
initializer = tf.keras.initializers.HeNormal()
serialized = serialize_initializer(initializer)
print("Serialized Initializer:", serialized)

deserialized = deserialize_initializer(serialized)
print("Deserialized Initializer:", deserialized)
