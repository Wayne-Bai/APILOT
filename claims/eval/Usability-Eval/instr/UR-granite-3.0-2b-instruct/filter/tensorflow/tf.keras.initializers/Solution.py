import tensorflow as tf

# Define a custom initializer
class MyInitializer(tf.keras.initializers.Initializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __call__(self, shape, dtype=None, **kwargs):
        # Custom initialization logic here
        return tf.random.uniform(shape, minval=-1.0, maxval=1.0, dtype=dtype)

# Create a model with the custom initializer
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, kernel_initializer=MyInitializer(), activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Save the model with the custom initializer
model.save('my_model')

# Load the model with the custom initializer
new_model = tf.keras.models.load_model('my_model')
