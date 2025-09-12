import tensorflow as tf

class DifferentiableGraphFunction(tf.Module):
    def __init__(self):
        super(DifferentiableGraphFunction, self).__init__()

    @tf.function
    def forward(self, inputs):
        """
        Define the forward pass of the graph function here.
        This method should be implemented by subclasses.
        """
        raise NotImplementedError("Subclasses should implement this method.")

    @tf.function
    def backward(self, inputs, output_grad):
        """
        Define the backward pass of the graph function here.
        This method should be implemented by subclasses.
        """
        raise NotImplementedError("Subclasses should implement this method.")
