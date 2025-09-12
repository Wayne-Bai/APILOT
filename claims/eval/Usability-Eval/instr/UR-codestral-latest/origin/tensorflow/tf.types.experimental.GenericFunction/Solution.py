import tensorflow as tf

# Defining a Base Class for Polymorphic Graph Functions
class GraphFunctionBase(tf.Module):
    @tf.function
    def compute(self, inputs):
        # The computation graph is defined here
        raise NotImplementedError('Child classes must implement this method.')
