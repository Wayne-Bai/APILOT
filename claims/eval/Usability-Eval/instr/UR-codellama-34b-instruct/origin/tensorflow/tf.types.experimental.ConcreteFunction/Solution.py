import tensorflow as tf

class DifferentiableGraphFunction(tf.keras.layers.Layer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.inputs = []
        self.outputs = []

    def build_graph(self):
        pass

    def call(self, inputs):
        if not self.built:
            self.build_graph()
        return self.compute(inputs)

    def compute(self, inputs):
        raise NotImplementedError("Subclasses must implement `compute`.")
