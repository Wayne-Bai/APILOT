import tensorflow as tf

# Define the initializer class
class ConstantInitializer(tf.keras.initializers.Initializer):
    def __init__(self, value=0.0):
        self.value = value

    def __call__(self, shape, dtype=None, partition_info=None):
        return tf.fill(shape, self.value)

# Create a model with the custom initializer
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(784,)),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compile the model with a loss function and an optimizer
model.compile(loss=tf.keras.losses.CategoricalCrossentropy(), optimizer=tf.keras.optimizers.Adam())
