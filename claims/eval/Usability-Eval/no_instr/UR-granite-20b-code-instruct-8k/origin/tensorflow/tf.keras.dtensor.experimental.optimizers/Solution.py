import tensorflow as tf

# Define the optimizer
optimizer = tf.keras.optimizers.Adam()

# Compile the model with the optimizer
model.compile(optimizer=optimizer)

# Train the model
model.fit(x_train, y_train, epochs=10)
