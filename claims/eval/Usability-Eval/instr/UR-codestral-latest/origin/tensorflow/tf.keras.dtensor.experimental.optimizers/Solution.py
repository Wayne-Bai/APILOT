import tensorflow as tf

# Create an Adam optimizer with a learning rate of 0.001
optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)

# Assume we have a model and some data
model = ...
data = ...
target = ...

# Training loop
with tf.GradientTape() as tape:
    predictions = model(data, training=True)
    loss = loss_object(target, predictions)
    gradients = tape.gradient(loss, model.trainable_variables)
    optimizer.apply_gradients(zip(gradients, model.trainable_variables))
