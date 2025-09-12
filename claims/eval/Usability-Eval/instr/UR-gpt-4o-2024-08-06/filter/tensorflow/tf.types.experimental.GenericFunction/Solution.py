import tensorflow as tf

class BaseGraphFunction:
    def __init__(self, name):
        # Initialize with a name for the function
        self.name = name
        self.graph = tf.Graph()

    def __enter__(self):
        # Enter the graph context
        self.graph.as_default().__enter__()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Exit the graph context
        self.graph.as_default().__exit__(exc_type, exc_value, traceback)

    def build(self):
        # Abstract method to be overridden
        raise NotImplementedError("Build method must be defined in subclasses")

    def run(self, session, feed_dict=None):
        # Run method to execute the graph
        with self.graph.as_default():
            self.build()
            init = tf.compat.v1.global_variables_initializer()
            session.run(init)
            return self.compute(session, feed_dict)

    def compute(self, session, feed_dict=None):
        # Placeholder for computation logic
        raise NotImplementedError("Compute method must be defined in subclasses")

    def __str__(self):
        return f"BaseGraphFunction(name={self.name})"


# Example subclass implementation
class AddGraphFunction(BaseGraphFunction):
    def __init__(self, name, a, b):
        super().__init__(name)
        self.a = a
        self.b = b
        self.result = None

    def build(self):
        # Define a tensor operation in the graph
        with self.graph.as_default():
            self.result = tf.add(self.a, self.b, name='add')

    def compute(self, session, feed_dict=None):
        # Compute the result of the graph operation
        return session.run(self.result, feed_dict=feed_dict)

# Usage example
if __name__ == "__main__":
    # Create TensorFlow session
    with tf.compat.v1.Session() as sess:
        with AddGraphFunction('add_example', tf.constant(5), tf.constant(3)) as add_func:
            result = add_func.run(sess)
            print(f'The result of the addition operation is: {result}')
