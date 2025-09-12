import tensorflow as tf

class GraphFunction(object):
    def __init__(self):
        self.graph = tf.Graph()
        self.session = tf.Session(graph=self.graph)

    def _build(self):
        raise NotImplementedError

    def build(self):
        with self.graph.as_default():
            self._build()
            self.session.run(tf.global_variables_initializer())

    def __call__(self, *args, **kwargs):
        with self.graph.as_default():
            return self.session.run(self(*args, **kwargs))
