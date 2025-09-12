import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

# Define the model architecture
model = Sequential([
    Dense(64, activation='relu', input_shape=(input_dim,)),
    Dense(64, activation='relu'),
    Dense(output_dim, activation='softmax')
])

# Compile the model
model.compile(optimizer=Adam(learning_rate=0.001),  # Use Adam optimizer
              loss='categorical_crossentropy',      # For classification with logits defines softmax
              metrics=['accuracy'])

# Define the model summary
model.summary()
