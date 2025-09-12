# Importing the required libraries
import tensorflow as tf

# Define a function to configure the model for training
def configure_model_for_training(model, learning_rate, optimizer_name, loss_name, metric_names):
    """
    Configures the model for training.

    Args:
    - model (tf.keras.Model): The Keras model instance.
    - learning_rate (float): The learning rate of the optimizer.
    - optimizer_name (str): The name of the optimizer to use.
    - loss_name (str): The name of the loss function to use.
    - metric_names (list[str]): The list of metric names to track.

    Returns:
    - None
    """

    # Specify the compiler
    compiler = model.compile(
        optimizer=tf.keras.optimizers.get(optimizer_name),
        loss=loss_name,
        metrics=metric_names
    )

    # Print the compiler summary
    print(f"Compiler: {compiler.__dict__}")

    # Print the model summary
    print(f"Model Summary:\n{model.summary()}")

    # Print the compiler compile train arguments
    print(f"Compile Train Args:\n{model.compile.__dict__}")

    # Print the optimizer section of the compiler
    print(f"Optimizer: {compiler.optimizer.__dict__}")

    # Print the optimizer configuration
    print(f"Optimizer Configuration:\n{compiler.optimizer.get_config()}")

    # Print the loss function section of the compiler
    print(f"Loss Function: {compiler.loss.__name__}")

    # Print the loss function configuration
    print(f"Loss Function Configuration: {loss_name}")

    # Print the metrics configuration
    print(f"Metrics Configuration: {metric_names}")


# Example usage:
# Define a sample model
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(784,)),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Configure the optimizer
optimizer_name = "adam"

# Configure the loss function
loss_name = "sparse_categorical_crossentropy"

# Configure the metrics
metric_names = ["accuracy"]

# Configure the model for training
configure_model_for_training(
    model=model,
    learning_rate=0.001,
    optimizer_name=optimizer_name,
    loss_name=loss_name,
    metric_names=metric_names,
)
