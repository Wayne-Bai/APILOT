import tensorflow as tf

class DifferentiableFunction(tf.Module):
    def __init__(self, name=None):
        super().__init__(name=name)
        # Any other initial setup if necessary

    @tf.function
    def __call__(self, *args, **kwargs):
        """
        This method should be overridden by subclasses to implement the specific
        logic of the differentiable function.
        """
        raise NotImplementedError("Subclasses must override __call__ method.")

    @tf.function
    def gradient(self, *args, **kwargs):
        """
        Computes the gradient of the function with respect to its inputs.

        Returns:
            gradients: The gradients of the output with respect to each input.
        """
        with tf.GradientTape() as tape:
            tape.watch(args)
            output = self.__call__(*args, **kwargs)
        gradients = tape.gradient(output, args)
        return gradients

# Example subclass implementing a specific differentiable function
class MyFunction(DifferentiableFunction):
    def __init__(self, coeff=1.0):
        super().__init__()
        self.coeff = coeff

    @tf.function
    def __call__(self, x):
        return self.coeff * x**2

# Example usage
my_func = MyFunction(coeff=2.0)
x = tf.constant(3.0)
y = my_func(x)
grad = my_func.gradient(x)

print("Function output:", y.numpy())
print("Gradient:", grad.numpy())
