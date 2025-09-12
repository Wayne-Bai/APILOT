
import tensorflow as tf
from tensorflow.keras import initializers

# Create a Keras initializer
initializer = initializers.RandomNormal(mean=0.0, stddev=0.05)

# Serialize the initializer
config = initializer.get_config()

# Deserialize the initializer
new_initializer = initializers.deserialize(config)

# Use the deserialized initializer in a layer
layer = tf.keras.layers.Dense(units=10, kernel_initializer=new_initializer)
