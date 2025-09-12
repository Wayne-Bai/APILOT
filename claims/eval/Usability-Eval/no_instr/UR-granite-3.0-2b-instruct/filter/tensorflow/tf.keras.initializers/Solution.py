import tensorflow as tf

# Define a custom initializer
class MyInitializer(tf.keras.initializers.Initializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __call__(self, shape, dtype=None, **kwargs):
        # Custom initialization logic here
        return tf.random.uniform(shape, minval=-1.0, maxval=1.0, dtype=dtype)

# Create a model with the custom initializer
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, initializer=MyInitializer(), activation='relu'),
    tf.keras.layers.Dense(10, initializer=MyInitializer(), activation='softmax')
])

# Serialize the model
model.save('my_model.h5')

# Deserialize the model
new_model = tf.keras.models.load_model('my_model.h5')
