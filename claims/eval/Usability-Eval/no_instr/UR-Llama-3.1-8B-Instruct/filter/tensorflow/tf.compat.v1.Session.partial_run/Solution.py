# Import the necessary libraries
import tensorflow as tf
import numpy as np

# Creating a simple model with a linear layer
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(1, input_shape=[1])
])

# Compile the model with an optimizer and a loss function
model.compile(optimizer='adam', loss='mean_squared_error')

# Generate some sample data
np.random.seed(0)
X = np.random.uniform(-10, 10, size=[100, 1])
y = np.random.uniform(-10, 10, size=[100, 1])

# Reshape the data
X = tf.cast(X, tf.float32)
y = tf.cast(y, tf.float32)

# Continue with the execution, start at index 50
start_index = 50
for i in range(start_index, len(X)):
    # Extract the current input and target
    current_input = X[i:i+1]
    current_target = y[i:i+1]
    
    # One-hot encoding is not required here as there is only one target value
    # Reshape the inputs to match the model's input shape
    current_input = tf.reshape(current_input, (-1,))
    
    # One step in the train loop
    with tf.GradientTape() as tape:
        prediction = model(tf.constant([current_input]))
        loss = tf.reduce_sum(tf.square(prediction - current_target))
    gradients = tape.gradient(loss, model.trainable_variables)
    model.optimizer.apply_gradients(zip(gradients, model.trainable_variables))
    
    print(f"Iteration {i+1}, Prediction: {prediction.numpy()[0][0]:.2f}, Target: {current_target.numpy()[0][0]:.2f}")
