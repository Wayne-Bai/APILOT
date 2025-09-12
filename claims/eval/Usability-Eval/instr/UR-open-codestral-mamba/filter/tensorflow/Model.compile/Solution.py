import tensorflow as tf

# Assuming we have inputs and targets variable for training
# inputs = tf.placeholder(...)
# targets = tf.placeholder(...)

# Define the model architecture (例如, 一个两层神经网络)
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(784,)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Define the optimizer and loss function
model.compile(
    optimizer=tf.keras.optimizers.Adam(0.01),
    loss=tf.keras.losses.CategoricalCrossentropy(from_logits=True),
    metrics=['accuracy']
)

# Now model.fit(inputs, targets, epochs=5) can be used to train the model
