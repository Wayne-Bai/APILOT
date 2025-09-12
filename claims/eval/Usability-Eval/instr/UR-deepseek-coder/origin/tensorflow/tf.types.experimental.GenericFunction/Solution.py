import tensorflow as tf

class GraphFunctionBase(tf.Module):
    def __init__(self, name=None):
        super(GraphFunctionBase, self).__init__(name=name)
        self._graph_function = None

    def build_graph(self):
        raise NotImplementedError("Subclasses should implement this method to build the graph.")

    def __call__(self, *args, **kwargs):
        if self._graph_function is None:
            self._graph_function = self.build_graph()
        return self._graph_function(*args, **kwargs)

# Example subclass implementation
class MyGraphFunction(GraphFunctionBase):
    def build_graph(self):
        @tf.function
        def my_graph(x):
            return x * 2
        return my_graph

# Usage example
my_function = MyGraphFunction()
result = my_function(tf.constant([1.0, 2.0, 3.0]))
print(result)  # Output: tf.Tensor([2. 4. 6.], shape=(3,), dtype=float32)
