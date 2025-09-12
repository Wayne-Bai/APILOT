import tensorflow as tf

class GraphFunction(tf.Module):
    """
    Base class for polymorphic graph functions.

    This class is designed to be inherited by specific graph functions.
    Each specific graph function should implement the `forward` method.

    Attributes:
        name (str): The name of the graph function.
        inputs (List[tf.Tensor]): The input tensors of the graph function.
        outputs (List[tf.Tensor]): The output tensors of the graph function.
    """

    def __init__(self, name=None):
        super().__init__(name=name)

    def forward(self, inputs):
        """
        Forward pass of the graph function.

        Args:
            inputs (List[tf.Tensor]): The input tensors.

        Returns:
            List[tf.Tensor]: The output tensors.
        """
        raise NotImplementedError("Subclass must implement the forward method.")

    def __call__(self, inputs):
        return self.forward(inputs)
