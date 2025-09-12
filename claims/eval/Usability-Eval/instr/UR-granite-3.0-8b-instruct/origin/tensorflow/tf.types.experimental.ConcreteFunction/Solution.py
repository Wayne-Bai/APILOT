import tensorflow as tf

class DifferentiableGraphFunction:
    def __init__(self):
        self.graph = tf.Graph()

    def build_graph(self, inputs, outputs):
        with self.graph.as_default():
            self.inputs = inputs
            self.outputs = outputs

    def differentiate(self, target):
        with tf.GradientTape() as tape:
            tape.watch(self.inputs)
            loss = tf.reduce_sum(tf.square(self.outputs - target))
        grads = tape.gradient(loss, self.inputs)
        return grads
