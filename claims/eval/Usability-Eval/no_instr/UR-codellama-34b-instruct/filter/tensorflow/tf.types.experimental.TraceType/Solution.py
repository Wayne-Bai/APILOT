
import tensorflow as tf

# Import the necessary functions from TensorFlow
from tensorflow.python.ops import array_ops, math_ops

@tf.function
def calculate_area(height: float, width: float) -> float:
    """Calculates the area of a rectangle given its height and width."""
    return height * width

@tf.function
def calculate_perimeter(height: float, width: float) -> float:
    """Calculates the perimeter of a rectangle given its height and width."""
    return 2 * (height + width)

# Test the functions with some examples
print(calculate_area(10.0, 5.0)) # Should output 50.0
print(calculate_perimeter(10.0, 5.0)) # Should output 30.0
