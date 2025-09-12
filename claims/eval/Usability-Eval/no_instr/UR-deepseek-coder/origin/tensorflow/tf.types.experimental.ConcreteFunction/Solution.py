import tensorflow as tf

class DifferentiableGraphFunction:
    def __init__(self, graph_def, input_names, output_names):
        self.graph_def = graph_def
        self.input_names = input_names
        self.output_names = output_names
        self.graph = self._build_graph()

    def _build_graph(self):
        graph = tf.Graph()
        with graph.as_default():
            tf.import_graph_def(self.graph_def, name='')
        return graph

    def __call__(self, inputs):
        with tf.Session(graph=self.graph) as sess:
            feed_dict = {self.graph.get_tensor_by_name(name + ':0'): value for name, value in zip(self.input_names, inputs)}
            outputs = sess.run(self.output_names, feed_dict=feed_dict)
        return outputs

    def gradient(self, inputs, output_index=0):
        with tf.Session(graph=self.graph) as sess:
            feed_dict = {self.graph.get_tensor_by_name(name + ':0'): value for name, value in zip(self.input_names, inputs)}
            output_tensor = self.graph.get_tensor_by_name(self.output_names[output_index] + ':0')
            grads = tf.gradients(output_tensor, [self.graph.get_tensor_by_name(name + ':0') for name in self.input_names])
            gradients = sess.run(grads, feed_dict=feed_dict)
        return gradients
