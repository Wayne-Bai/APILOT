import tensorflow as tf

# Define the model architecture
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(32,)),  # Input layer
    tf.keras.layers.Dense(64, activation='relu'),  # Hidden layer
    tf.keras.layers.Dense(10, activation='softmax')  # Output layer
])

# Compile the model
model.compile(optimizer=tf.optimizers.Adam( learning_rate=0.001 ),
              loss='categorical_crossentropy',
              metrics=['accuracy'])
