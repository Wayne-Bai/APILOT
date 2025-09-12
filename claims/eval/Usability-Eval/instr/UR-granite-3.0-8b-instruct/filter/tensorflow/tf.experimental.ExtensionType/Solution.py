import tensorflow as tf

class TensorFlowExtensionTypeBase:
    def __init__(self):
        self.graph = tf.Graph()

    def build_graph(self):
        raise NotImplementedError("Subclasses must implement this method")

    def run_graph(self, input_data):
        with self.graph.as_default():
            output = self.build_graph(input_data)
            with tf.Session() as sess:
                return sess.run(output)
