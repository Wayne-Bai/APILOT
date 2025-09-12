import tensorflow as tf
from tensorflow.keras.initializers import VarianceScaling

# Define a custom Keras initializer
initializer = VarianceScaling(scale=2.0, mode='fan_in', distribution='truncated_normal')

# Serialize the initializer to a config dictionary
config = tf.keras.initializers.serialize(initializer)

# Deserialize the initializer from the config dictionary
deserialized_initializer = tf.keras.initializers.deserialize(config)

# Check if the initializer was correctly deserialized
print("Original initializer:")
print(initializer)
print("\nDeserialized initializer:")
print(deserialized_initializer)
