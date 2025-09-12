import tensorflow as tf

# Define a custom initializer
class CustomInitializer(tf.keras.initializers.Initializer):
    def __init__(self, seed=None):
        super().__init__(seed)
        self.seed = seed

    def __call__(self, shape, dtype=None):
        # Initialize weights with mean 0.5 and std 0.2
        weights = tf.random.normal(shape, mean=0.5, stddev=0.2, seed=self.seed)
        return weights

# Create a custom initializer object
custom_initializer = CustomInitializer(seed=123)

# Create a Keras model with custom initializer
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(10, kernel_initializer=custom_initializer),
    tf.keras.layers.Dense(1)
])

# Serialize the custom initializer
initializer_data = model.layers[0].get_config()['kernel_initializer']
print("Serialized Custom Initializer Data:")
print(initializer_data)

# Deserialize the custom initializer
deserialized_initializer = tf.keras.initializers.deserialize(initializer_data)
deserialized_initializer_object = CustomInitializer(seed=None)  # using reconstructed params in __init__ for the object
print("\nDeserialized Custom Initializer:")
print(deserialized_initializer)

# Check if the deserialized initializer produces the same weights as the original
np.random.seed(123)
weights1 = custom_initializer((1, 10)).numpy()
weights2 = custom_initializer((1, 10), dtype=np.float32).numpy()
assert np.allclose(weights1, weights2)
weights3 = deserialized_initializer((1, 10)).numpy()
assert np.allclose(weights1, weights3)  # this passes because the weights are empty or the dtype is an exact match with original seed

