
import tensorflow as tf

class DifferentiableGraphFunction(tf.Module):
    def __init__(self):
        super(DifferentiableGraphFunction, self).__init__()

    def __call__(self, x):
        raise NotImplementedError("Subclasses must implement this method")
