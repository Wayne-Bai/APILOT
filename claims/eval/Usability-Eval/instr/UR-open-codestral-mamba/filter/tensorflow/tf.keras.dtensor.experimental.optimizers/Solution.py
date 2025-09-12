import tensorflow as tf

# Define a simple model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(784,)),
    tf.keras.layers.Dense(10)
])

# Define our optimizer
optimizer = tf.keras.optimizers.Adam(1e-3)

# Define our loss function
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

# Define our metrics
metrics = ['accuracy']

# Compile our model
model.compile(optimizer=optimizer, loss=loss_fn, metrics=metrics)

# Display the model's architecture
model.summary()
