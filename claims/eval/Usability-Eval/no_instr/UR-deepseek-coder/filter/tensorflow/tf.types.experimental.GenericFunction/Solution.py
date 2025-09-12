import tensorflow as tf

class GraphFunctionBase:
    def __init__(self, input_signature):
        self.input_signature = input_signature
        self.graph_function = None

    def _build_graph_function(self):
        @tf.function(input_signature=self.input_signature)
        def graph_function(*args):
            return self._execute(*args)
        return graph_function

    def _execute(self, *args):
        raise NotImplementedError("Subclasses must implement this method")

    def __call__(self, *args):
        if self.graph_function is None:
            self.graph_function = self._build_graph_function()
        return self.graph_function(*args)

# Example subclass
class AddFunction(GraphFunctionBase):
    def __init__(self):
        super().__init__([tf.TensorSpec(shape=None, dtype=tf.float32, name="x"),
                          tf.TensorSpec(shape=None, dtype=tf.float32, name="y")])

    def _execute(self, x, y):
        return x + y

# Usage
add_func = AddFunction()
result = add_func(tf.constant(2.0), tf.constant(3.0))
print(result.numpy())  # Output: 5.0
