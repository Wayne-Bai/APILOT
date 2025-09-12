import tensorflow as tf
import tensorboard

# Create a TensorBoard instance
tb = tensorboard.SummaryWriter('logs')

# Define a simple model
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(784,)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=5, batch_size=32)

# Write the summaries to TensorBoard
tb.add_summary(model.history.history, step=0)

# Start the TensorBoard server
tf.app.run(main=[None, '-m', 'tensorboard', '--logdir', 'logs'])
