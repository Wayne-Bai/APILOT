
import tensorflow as tf
from tensorflow.keras import layers

# Define the Keras initializer
init = layers.VarianceScaling(scale=2.0, mode='fan_avg', distribution='normal')

# Serialize the initializer
serialized_init = tf.keras.utils.serialize_initializer(init)

# Deserialize the initializer
deserialized_init = tf.keras.utils.deserialize_initializer(serialized_init)

# Use the deserialized initializer to create a new layer
layer = layers.Dense(64, activation='relu', kernel_initializer=deserialized_init)
