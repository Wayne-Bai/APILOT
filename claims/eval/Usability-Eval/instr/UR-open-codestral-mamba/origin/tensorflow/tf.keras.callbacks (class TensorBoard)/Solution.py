import tensorflow as tf

# Create a simple model to demonstrate visualization in TensorBoard

# Define the model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(32, activation='relu', input_shape=(784,)),  # Input shape required
    tf.keras.layers.Dense(10, activation='softmax')
])

# Define a loss function and a optimizer
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
optimizer = tf.keras.optimizers.Adam()

# Compile the model
model.compile(optimizer=optimizer,
              loss=loss_fn,
              metrics=['accuracy'])

# Create a summary to visualize with TensorBoard
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir='./logs', histogram_freq=1)

# Train the model
model.fit(x_train, y_train, epochs=5, callbacks=[tensorboard_callback])
