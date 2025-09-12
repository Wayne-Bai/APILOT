import tensorflow as tf

# Define the model
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Define the optimizer
optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)

# Compile the model
model.compile(optimizer=optimizer, loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Define the checkpoint
checkpoint = tf.keras.callbacks.ModelCheckpoint('model.h5', save_weights_only=True, verbose=1)

# Train the model
model.fit(x_train, y_train, epochs=10, callbacks=[checkpoint])
