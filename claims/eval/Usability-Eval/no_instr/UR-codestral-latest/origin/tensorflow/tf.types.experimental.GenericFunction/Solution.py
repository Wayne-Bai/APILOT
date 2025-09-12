import tensorflow as tf

class GraphFunctionBase(object):
    def __init__(self, *inputs):
        self._inputs = inputs

    @tf.function
    def __call__(self, *args, **kwargs):
        raise NotImplementedError("Subclasses must override __call__.")
