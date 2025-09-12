import tensorflow as tf

# Define a simple model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Define the checkpoint
checkpoint = tf.train.Checkpoint(optimizer=tf.keras.optimizers.Adam(),
                                 model=model)

# Define a function to train the model and save the checkpoint
def train_and_save(epochs):
    # Compile the model
    model.compile(optimizer=tf.keras.optimizers.Adam(),
                  loss=tf.keras.losses.SparseCategoricalCrossentropy(),
                  metrics=['accuracy'])

    # Train the model
    model.fit(x_train, y_train, epochs=epochs)

    # Save the checkpoint
    checkpoint.save('model_checkpoint')

# Call the function to train and save the model
train_and_save(10)
