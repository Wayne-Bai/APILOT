
import tensorflow as tf

class DifferentiableGraphFunction(tf.Module):
    def __init__(self):
        super(DifferentiableGraphFunction, self).__init__()

    def forward(self, x):
        raise NotImplementedError("Subclasses must implement this method")

    def gradient(self, x):
        with tf.GradientTape() as tape:
            tape.watch(x)
            y = self.forward(x)
        return tape.gradient(y, x)
