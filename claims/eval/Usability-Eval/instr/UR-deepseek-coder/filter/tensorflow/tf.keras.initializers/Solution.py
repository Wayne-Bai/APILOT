import tensorflow as tf
from tensorflow.keras import initializers

# Define a custom initializer
class CustomInitializer(initializers.Initializer):
    def __call__(self, shape, dtype=None):
        return tf.random.normal(shape, mean=0.0, stddev=0.05, dtype=dtype)

# Serialize the custom initializer
serialized_initializer = initializers.serialize(CustomInitializer())

# Deserialize the custom initializer
deserialized_initializer = initializers.deserialize(serialized_initializer)

# Example usage in a Keras layer
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, kernel_initializer=deserialized_initializer, activation='relu'),
    tf.keras.layers.Dense(10, kernel_initializer=deserialized_initializer, activation='softmax')
])

# Compile and train the model (example)
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
# model.fit(x_train, y_train, epochs=5)
