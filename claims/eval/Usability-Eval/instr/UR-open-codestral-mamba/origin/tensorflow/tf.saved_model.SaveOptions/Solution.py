import tensorflow as tf

# Define a simple model
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(3, activation='relu', input_shape=(784,)),
    tf.keras.layers.Dense(3)
])

# Define the optimizer
opt = tf.keras.optimizers.Adam(learning_rate=0.01)

# Compile the model
model.compile(optimizer=opt,
              loss=tf.keras.losses.CategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=10, validation_data=(x_val, y_val))

# Save the entire model
model.save('my_model')
