import tensorflow as tf

# Create a Keras initializer
initializer = tf.keras.initializers.GlorotUniform()

# Serialize the initializer
serialized_initializer = tf.keras.initializers.serialize(initializer)

# Print the serialized form of the initializer
print("Serialized Initializer:", serialized_initializer)

# Deserialize the initializer
deserialized_initializer = tf.keras.initializers.deserialize(serialized_initializer)

# Print deserialized initializer to verify
print("Deserialized Initializer:", deserialized_initializer)
