import tensorflow as tf
from abseil import tf_required
from tensorflow import keras

# Defining a base class for differentiable graph functions
class DifferentiableGraph(tf.Module):
    """
    Base class for differentiable graph functions.

    This class serves as a base for creating differentiable graph functions. It
    provides a basic structure for defining graph functions and their derivatives.

    Attributes:
        inputs: A list of input tensors for the graph function.
        outputs: The output tensor of the graph function.
        params: A dictionary of trainable parameters for the graph function.
    """

    def __init__(self, inputs):
        """
        Initializes the DifferentiableGraph object.

        Args:
            inputs: A list of input tensors for the graph function.
        """
        super().__init__()
        self.inputs = inputs
        self.params = {}

    @tf_required
    def call(self, inputs):
        """
        Defines the graph function.

        This method is required to be implemented by subclasses.

        Args:
            inputs: A list of input tensors for the graph function.
        """
        raise NotImplementedError

    def add_parameter(self, name, shape, init_value=None):
        """
        Adds a trainable parameter to the graph function.

        Args:
            name: The name of the parameter.
            shape: The shape of the parameter.
            init_value: The initial value of the parameter. Defaults to None.
        """
        if name in self.params:
            raise ValueError(f"Parameter '{name}' already exists.")
        self.params[name] = tf.Variable(init_value or tf.zeros(shape), name=name)

    def get_parameter(self, name):
        """
        Gets a trainable parameter from the graph function.

        Args:
            name: The name of the parameter.

        Returns:
            The trainable parameter.
        """
        return self.params.get(name)

class MyGraph(DifferentiableGraph):
    """
    A simple example of a differentiable graph function.
    """

    def __init__(self, inputs):
        super().__init__(inputs)
        self.add_parameter("weight", (3,))

    @tf_required
    def call(self, inputs):
        weight = self.get_parameter("weight")
        return tf.matmul(inputs, weight)

graph = MyGraph(tf.ones((2, 2)))
print(graph.call(graph.inputs).numpy())
