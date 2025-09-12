import tensorflow as tf

# Define a Keras initializer
initializer = tf.keras.initializers.GlorotUniform()

# Serialize the initializer
serialized_init = tf.keras.initializers.serialize(initializer)

# Deserialize the initializer
deserialized_init = tf.keras.initializers.deserialize(serialized_init)

# Show both serialized and deserialized outputs
print("Serialized initializer:", serialized_init)
print("Deserialized initializer:", deserialized_init)
