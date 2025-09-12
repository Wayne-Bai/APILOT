import tensorflow as tf

class BaseGraphFunction:
    def __init__(self):
        pass

    def build(self):
        raise NotImplementedError("Should implement build method")

    def call(self, inputs):
        raise NotImplementedError("Should implement call method")

class LinearGraphFunction(BaseGraphFunction):
    def __init__(self, units):
        super().__init__()
        self.units = units

    def build(self):
        self.weights = self.add_weight(name='weights',
                                       shape=[self.units],
                                       initializer='glorot_uniform',
                                       trainable=True)
        self.biases = self.add_weight(name='biases',
                                      shape=[self.units],
                                      initializer='zeros',
                                      trainable=True)

    def call(self, inputs):
        return tf.matmul(inputs, self.weights) + self.biases

class AddGraphFunction(BaseGraphFunction):
    def __init__(self, units):
        super().__init__()
        self.units = units

    def build(self):
        self.weights = self.add_weight(name='weights',
                                       shape=[self.units, self.units],
                                       initializer='glorot_uniform',
                                       trainable=True)
        self.biases = self.add_weight(name='biases',
                                      shape=[self.units],
                                      initializer='zeros',
                                      trainable=True)

    def call(self, inputs):
        return tfypad(inputs, self.weights) + self.biases

# Example of using the classes
inputs = tf.random.normal([10, 3])

linear_function = LinearGraphFunction(4)
add_function = AddGraphFunction(4)

linear_function.build()
add_function.build()

linear_output = linear_function(inputs)
add_output = add_function(linear_output)

print("Linear Function Output:\n", linear_output)
print("Add Function Output:\n", add_output)
