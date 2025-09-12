import tensorflow as tf

class BaseGraphFunction(tf.Module):
    def __init__(self, name=None):
        super().__init__(name=name)

    def call(self, *args, **kwargs):
        raise NotImplementedError("Subclasses should implement this method")

class AddGraphFunction(BaseGraphFunction):
    def call(self, x, y):
        return tf.add(x, y)

class MultiplyGraphFunction(BaseGraphFunction):
    def call(self, x, y):
        return tf.multiply(x, y)

# Example usage
if __name__ == "__main__":
    add_function = AddGraphFunction()
    multiply_function = MultiplyGraphFunction()

    x = tf.constant(3)
    y = tf.constant(5)

    print("Addition Result:", add_function(x, y).numpy())
    print("Multiplication Result:", multiply_function(x, y).numpy())
