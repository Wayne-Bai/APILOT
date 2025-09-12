import tensorflow as tf

# Define the model
model = tf.keras.models.Sequential([
  tf.keras.layers.Dense(256, activation='relu'),
  tf.keras.layers.Dense(256, activation='relu'),
  tf.keras.layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer=tf.keras.optimizers.Adam(0.001),
              loss=tf.keras.losses.CategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# Then, you can use the built-in "tensorboard" callback to enable visualizations for TensorBoard

callbacks = [
    tf.keras.callbacks.TensorBoard(log_dir='./log',
                                   histogram_freq=1,
                                   embeddings_freq=1,
                                   update_freq='epoch')
]

# Fit the model
history = model.fit(train_data, train_labels,
                    epochs=10,
                    validation_data=(test_data, test_labels),
                    callbacks=callbacks)
