
import tensorflow as tf

# Create a simple sequential model
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(784,)),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Serialize the model's initializers
serialized_initializers = tf.keras.models.serialize(model.weights)
print(serialized_initializers)

# Deserialize the initializers
deserialized_initializers = tf.keras.models.deserialize(serialized_initializers, model.weights)
print(deserialized_initializers)
