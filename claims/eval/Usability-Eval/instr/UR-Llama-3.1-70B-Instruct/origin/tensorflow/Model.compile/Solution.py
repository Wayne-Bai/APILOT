# Import necessary libraries
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

# Define the model architecture
def create_model(input_dim, output_dim):
    model = Sequential()
    model.add(Dense(64, activation='relu', input_dim=input_dim))
    model.add(Dropout(0.5))
    model.add(Dense(32, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(output_dim, activation='softmax'))
    return model

# Configure the model for training
def configure_model(model, loss, optimizer, metrics):
    model.compile(loss=loss, optimizer=optimizer, metrics=metrics)
    return model

# Example usage
if __name__ == "__main__":
    # Define the input and output dimensions
    input_dim = 784
    output_dim = 10

    # Create the model
    model = create_model(input_dim, output_dim)

    # Configure the model for training
    loss = tf.keras.losses.SparseCategoricalCrossentropy()
    optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)
    metrics = ['accuracy']
    model = configure_model(model, loss, optimizer, metrics)

    # Print the model summary
    model.summary()
