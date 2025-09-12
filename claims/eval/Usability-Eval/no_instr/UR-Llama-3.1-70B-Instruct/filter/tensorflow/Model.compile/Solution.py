# Importing necessary libraries
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Configuring the model for training
def configure_model_for_training(model):
    """
    This function configures the model for training by compiling it with a loss function, 
    an optimizer and evaluation metrics.
    
    Args:
        model (tf.keras.Model): The model to be configured.
    
    Returns:
        tf.keras.Model: The configured model.
    """
    # Compile the model
    model.compile(
        loss='sparse_categorical_crossentropy',  # Loss function
        optimizer=keras.optimizers.Adam(),  # Optimizer
        metrics=['accuracy']  # Evaluation metrics
    )
    
    return model

# Example usage
if __name__ == "__main__":
    # Create a simple neural network model
    model = keras.Sequential([
        layers.Flatten(input_shape=(28, 28)),
        layers.Dense(128, activation='relu'),
        layers.Dense(10, activation='softmax')
    ])

    # Configure the model for training
    model = configure_model_for_training(model)
    
    # Print the model summary
    print(model.summary())
