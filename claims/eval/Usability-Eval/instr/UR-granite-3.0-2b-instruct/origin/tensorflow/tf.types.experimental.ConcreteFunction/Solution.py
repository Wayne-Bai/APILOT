import tensorflow as tf

class BaseGraphFunction:
    def __init__(self):
        self.input_tensors = []

    def add_input(self, tensor):
        self.input_tensors.append(tensor)

    def build_graph(self):
        raise NotImplementedError("Subclasses must implement this method")

    def call(self, *args, **kwargs):
        self.build_graph()
        return self._compute_output()

    def _compute_output(self):
        raise NotImplementedError("Subclasses must implement this method")
