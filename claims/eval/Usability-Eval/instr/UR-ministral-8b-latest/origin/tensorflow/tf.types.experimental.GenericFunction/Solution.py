import tensorflow as tf

class GraphFunctionBase:
    def __init__(self, input_tensor):
        self.input_tensor = input_tensor

    def build_graph(self):
        raise NotImplementedError("Subclasses should implement this method")

    def run_graph(self, session):
        try:
            result = session.run(self.build_graph(), feed_dict={self.input_tensor: self.input_tensor.eval()})
        except Exception as e:
            raise RuntimeError(f"Error occurred while running the graph: {str(e)}")
        return result

# Example subclass that implements GraphFunctionBase
class ExampleGraph(GraphFunctionBase):
    def build_graph(self):
        # Define a simple graph that adds 10 to the input tensor and returns the result
        return tf.add(self.input_tensor, 10)

# Example usage
if __name__ == "__main__":
    input_tensor = tf.placeholder(dtype=tf.float32, shape=[None], name='input_tensor')
    example_graph = ExampleGraph(input_tensor)

    with tf.Session() as session:
        tf.global_variables_initializer().run()
        result = example_graph.run_graph(session)
        print(f"Result: {result}")
