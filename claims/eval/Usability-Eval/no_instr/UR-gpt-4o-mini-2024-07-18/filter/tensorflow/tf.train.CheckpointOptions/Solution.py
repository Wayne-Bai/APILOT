import tensorflow as tf

# Create a model for demonstration
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu', input_shape=(784,)),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', 
              loss='sparse_categorical_crossentropy', 
              metrics=['accuracy'])

# Create a directory to save checkpoints
checkpoint_dir = './checkpoints'
checkpoint_prefix = checkpoint_dir + '/ckpt'

# Create a callback to save the model checkpoints
checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
    filepath=checkpoint_prefix,
    save_weights_only=True,
    save_best_only=True,
    monitor='val_loss',
    mode='min'
)

# Training the model with checkpoints
# (X_train, y_train) should be your training data
# (X_val, y_val) should be your validation data
# For example:
# model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=10, callbacks=[checkpoint_callback])
