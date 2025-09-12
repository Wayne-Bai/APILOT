import tensorflow as tf
from tensorflow.core.framework import graph_pb2

def serialize_tensorflow_model(model):
    """
    Serialize a TensorFlow model into a Protobuf binary string representation.

    Args:
        model (tf.keras.Model): The TensorFlow model to serialize.

    Returns:
        bytes: The serialized model as a Protobuf binary string representation.
    """
    # Convert the model to a graph
    with tf.keras.backend.get_session().graph.as_default():
        tf.identity(model.outputs)

    # Get the graph definition
    graph_def = tf.keras.backend.get_session().graph_def

    # Serialize the graph definition to a binary string
    serialized_model = graph_def.SerializeToString()

    return serialized_model

# Example usage:
if __name__ == "__main__":
    # Create a simple model
    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(64, activation='relu', input_shape=(784,)),
        tf.keras.layers.Dense(32, activation='relu'),
        tf.keras.layers.Dense(10, activation='softmax')
    ])

    # Serialize the model
    serialized_model = serialize_tensorflow_model(model)

    # Print the serialized model (in bytes)
    print(serialized_model)
