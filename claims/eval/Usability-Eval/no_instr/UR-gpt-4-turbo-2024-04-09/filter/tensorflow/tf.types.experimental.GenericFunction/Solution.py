import tensorflow as tf

class BasePolymorphicFunction(tf.Module):
    def __init__(self, name=None):
        super().__init__(name=name)

    def compute(self, inputs):
        raise NotImplementedError("Subclasses must implement this method.")

# Example subclass implementing the base class
class SquareFunction(BasePolymorphicFunction):
    def compute(self, inputs):
        return tf.square(inputs)

# Example usage
if __name__ == "__main__":
    poly_func = SquareFunction()
    x = tf.constant([2, 3, 4], dtype=tf.float32)
    result = poly_func.compute(x)
    print("Result:", result.numpy())
