
import tensorflow as tf

# Define a simple sequential model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(784,)),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compile the model with a loss function and optimizer
model.compile(loss=tf.keras.losses.SparseCategoricalCrossentropy(), optimizer=tf.keras.optimizers.Adam())

# Define a callback for saving the model weights every 100 batches
class SaveCallback(tf.keras.callbacks.Callback):
    def on_batch_end(self, batch, logs={}):
        if batch % 100 == 0:
            self.model.save_weights('checkpoint')

# Add the callback to the model
model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test), callbacks=[SaveCallback()])
