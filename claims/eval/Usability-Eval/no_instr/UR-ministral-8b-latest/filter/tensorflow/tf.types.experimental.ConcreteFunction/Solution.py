import tensorflow as tf

class DifferentiableFunction(tf.Module):
    def __call__(self, *args, **kwargs):
        raise NotImplementedError("Subclasses should implement this!")

    def compute_derivative(self):
        raise NotImplementedError("Subclasses should implement this!")

# Example subclass
class ExampleFunction(DifferentiableFunction):
    def __init__(self, x):
        self.x = x

    def __call__(self, y):
        return self.x + y

    def compute_derivative(self, y):
        return tf.ones_like(self.x)

# Example usage
example_function = ExampleFunction(5)
result = example_function(10)
print("Result:", result.numpy())

# Compute derivative
derivative = example_function.compute_derivative(result).numpy()
print("Derivative:", derivative)
