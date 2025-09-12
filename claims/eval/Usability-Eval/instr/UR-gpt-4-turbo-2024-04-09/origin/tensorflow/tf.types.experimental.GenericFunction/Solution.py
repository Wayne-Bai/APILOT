import tensorflow as tf

class BaseGraphFunction(tf.Module):
    def __init__(self, name=None):
        super(BaseGraphFunction, self).__init__(name=name)

    def build_graph(self, inputs):
        raise NotImplementedError("Must implement build_graph method")

# Example derived class implementing the base class
class SpecificGraphFunction(BaseGraphFunction):
    def __init__(self, name=None):
        super(SpecificGraphFunction, self).__init__(name=name)

    def build_graph(self, inputs):
        return tf.square(inputs) + tf.cos(inputs)

# Using the classes
if __name__ == "__main__":
    graph_function = SpecificGraphFunction(name="MyGraphFunction")
    inputs = tf.constant([1.0, 2.0, 3.0])
    outputs = graph_function.build_graph(inputs)
    print(outputs)
