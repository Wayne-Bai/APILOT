import tensorflow as tf

class BaseGraphFunction:
    def __init__(self):
        self.inputs = []
        self.outputs = []

    def add_input(self, input):
        self.inputs.append(input)

    def add_output(self, output):
        self.outputs.append(output)

    def build_graph(self):
        raise NotImplementedError

    def compute_output(self):
        raise NotImplementedError

    def call(self, inputs):
        self.build_graph()
        output = self.compute_output()
        return output
