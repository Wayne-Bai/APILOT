import tensorflow as tf

class DifferentiableGraphFunction:
    def __init__(self, graph_function):
        self.graph_function = graph_function

    def __call__(self, *args, **kwargs):
        with tf.GradientTape() as tape:
            tape.watch(args)
            tape.watch(kwargs)
            result = self.graph_function(*args, **kwargs)
        gradient = tape.gradient(result, [arg for arg in args] + [kwargs[key] for key in kwargs])
        return result, gradient
