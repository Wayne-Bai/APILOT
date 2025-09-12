# Importing necessary libraries
import tensorflow as tf

class DifferentiableGraphFunction(tf.Module):
    """
    Base class for differentiable graph functions.
    
    This class provides a basic implementation of a differentiable graph function 
    in TensorFlow. It can be used as a base class for more complex graph functions.
    """
    
    def __init__(self, *args, **kwargs):
        """
        Initializes the DifferentiableGraphFunction.
        
        Args:
            *args: Variable number of positional arguments.
            **kwargs: Variable number of keyword arguments.
        """
        super().__init__(*args, **kwargs)
    
    def _build(self, input_values):
        """
        Builds the differentiable graph function.
        
        This method should be overridden by child classes to implement the logic 
        of their specific function. The input values are provided as a Tensor or 
        other types of data supported by TensorFlow.
        
        Args:
            input_values: The input values of the function.
        
        Returns:
            The output of the function.
        """
        raise NotImplementedError
    
    def call(self, input_values, *args, **kwargs):
        """
        Calls the differentiable graph function.
        
        This method delegates the call to the built method. It is a synonym for 
        calling the function with no arguments.
        
        Args:
            input_values: The input values of the function.
        
        Returns:
            The output of the function.
        """
        return self._build(input_values)


# Example usage:
class SquareFunction(DifferentiableGraphFunction):
    """
    A simple square function.
    
    This class inherits from DifferentiableGraphFunction and overrides the _build 
    method to implement the square function.
    """
    
    def _build(self, input_values):
        """
        Builds the square function.
        
        Args:
            input_values: The input values of the function.
        
        Returns:
            The square of the input value.
        """
        return tf.square(input_values)


# Create an instance of the SquareFunction
square_function = SquareFunction()

# Create an input tensor
input_tensor = tf.constant([1.0, 2.0, 3.0])

# Call the square function
output = square_function(input_tensor)

print(output)  # Output: [1. 4. 9.]
