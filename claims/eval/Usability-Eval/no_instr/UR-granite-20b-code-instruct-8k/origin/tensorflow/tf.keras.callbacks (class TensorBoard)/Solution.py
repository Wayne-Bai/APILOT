import tensorflow as tf

# Enable TensorBoard visualizations
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir='./logs')

# Add the callback to the model
model.fit(x_train, y_train, callbacks=[tensorboard_callback])
