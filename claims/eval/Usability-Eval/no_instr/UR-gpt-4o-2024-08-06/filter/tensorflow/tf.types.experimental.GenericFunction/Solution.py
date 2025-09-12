import tensorflow as tf

class BaseGraphFunction:
    """
    Base class for polymorphic graph functions. This class provides the foundational
    structure for creating graph functions that can be polymorphically extended.
    """

    def __init__(self, name="BaseGraphFunction"):
        self.name = name
        self._graph = tf.Graph()
        self._build_graph()

    def _build_graph(self):
        """
        This method should be overridden by subclasses to define their own computation graph.
        """
        with self._graph.as_default():
            self.input_placeholder = tf.placeholder(dtype=tf.float32, shape=[None], name="input")
            self.output_tensor = self.input_placeholder  # By default, no operation is applied
            self._initialize_graph()
    
    def _initialize_graph(self):
        """
        Optional method for any initialization tasks a graph might require.
        """
        pass

    def run(self, input_data):
        """
        Method to run the graph with given input data.
        """
        with tf.Session(graph=self._graph) as sess:
            feed_dict = {self.input_placeholder: input_data}
            result = sess.run(self.output_tensor, feed_dict=feed_dict)
        return result

# Example subclass implementing a squared operation
class SquareGraphFunction(BaseGraphFunction):
    def _build_graph(self):
        """
        Overrides the base method to build a graph that computes the square of input.
        """
        with self._graph.as_default():
            self.input_placeholder = tf.placeholder(dtype=tf.float32, shape=[None], name="input")
            self.output_tensor = tf.square(self.input_placeholder)
            self._initialize_graph()

# Example usage
if __name__ == "__main__":
    square_function = SquareGraphFunction("SquareFunction")
    input_data = [1.0, 2.0, 3.0]
    result = square_function.run(input_data)
    print("Squared results:", result)
