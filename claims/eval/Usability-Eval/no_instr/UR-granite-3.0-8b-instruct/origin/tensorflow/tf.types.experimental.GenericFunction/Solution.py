import tensorflow as tf

class GraphFunction:
    def __init__(self):
        self.graph = tf.Graph()

    def add_node(self, node_name, node_op):
        with self.graph.as_default():
            node = tf.ops.convert_to_tensor(node_op)
            self.graph.add_to_collection(node_name, node)

    def run(self, input_data):
        with self.graph.as_default():
            output = self.graph.get_tensor_by_name(self.graph.unique_name(input_data))
            return output.eval(session=tf.Session())
