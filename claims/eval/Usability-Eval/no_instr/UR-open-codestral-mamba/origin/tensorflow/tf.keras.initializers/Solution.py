import tensorflow as tf
from tensorflow.keras import initializers

# Define a custom initializer
initializer = initializers.RandomNormal(mean=0., stddev=1.)

# Serialize the initializer
initializer_config = tf.keras.initializers.serialize(initializer)

# Deserialize the initializer
deserialized_initializer = tf.keras.initializers.deserialize(initializer_config)

# Check if the initializer has been deserialized correctly
print('Original initializer:', initializer)
print('Deserialized initializer:', deserialized_initializer)

# Test the initializers
x = tf.keras.backend.variable(initializer(shape=(2, 2)))
deserialized_x = tf.keras.backend.variable(deserialized_initializer(shape=(2, 2)))

print('Original initializer output:', x.numpy())
print('Deserialized initializer output:', deserialized_x.numpy())
