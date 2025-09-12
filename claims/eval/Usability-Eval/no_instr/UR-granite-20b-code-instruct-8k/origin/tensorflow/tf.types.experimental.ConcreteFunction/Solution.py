import tensorflow as tf

class DifferentiableGraphFunction(object):
    """Base class for differentiable graph functions."""

    def __init__(self):
        """Initialize the differentiable graph function."""
        pass

    def __call__(self, *args, **kwargs):
        """Call the differentiable graph function."""
        pass

    def gradient(self, *args, **kwargs):
        """Compute the gradient of the differentiable graph function."""
        pass
