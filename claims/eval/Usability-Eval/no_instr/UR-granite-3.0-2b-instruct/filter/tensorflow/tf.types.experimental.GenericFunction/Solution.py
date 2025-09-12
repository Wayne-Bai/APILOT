import tensorflow as tf

class BaseGraphFunction:
    def __init__(self):
        self.graph = tf.Graph()

    def create_graph(self):
        raise NotImplementedError("Subclass must implement this method")

    def run_graph(self, session):
        raise NotImplementedError("Subclass must implement this method")

class MyGraphFunction(BaseGraphFunction):
    def create_graph(self):
        with self.graph.as_default():
            self.x = tf.placeholder(tf.float32)
            self.y = tf.add(self.x, 1.0)

    def run_graph(self, session):
        with session.as_default():
            result = session.run(self.y, feed_dict={self.x: 5.0})
        return result

# Usage
tf.compat.v1.disable_eager_execution()
graph_function = MyGraphFunction()
with tf.compat.v1.Session() as session:
    result = graph_function.run_graph(session)
    print(result)
