import tensorflow as tf

# Enable MLIR-Based TensorFlow Compiler Optimizations.
tf.config.optimizer.set_jit(True)

# Next, you can define and compile your TensorFlow model as usual.
# Here's a simple example of a model:

model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(784,)),
    tf.keras.layers.Dense(10)
])

model.compile(optimizer=tf.keras.optimizers.Adam(0.001),
              loss=tf.keras.losses.CategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])
