import tensorflow as tf

def my_python_function(x, y):
    """
    A simple python function that adds two numbers.
    
    Args:
    x (float): The first number.
    y (float): The second number.
    
    Returns:
    float: The sum of x and y.
    """
    return x + y

# Create a TensorFlow operation from the python function
def tf_wrapper(py_func, inp):
    """
    A TensorFlow operation that wraps the python function.
    
    Args:
    py_func (function): The python function to wrap.
    inp (list): A list of inputs to the python function.
    
    Returns:
    tf.Tensor: The result of the python function as a TensorFlow tensor.
    """
    return tf.py_function(py_func, inp, tf.float32)

# Example usage:
x = tf.constant(2.0)
y = tf.constant(3.0)

# Call the python function using the TensorFlow operation
result = tf_wrapper(my_python_function, [x, y])

print(result)
