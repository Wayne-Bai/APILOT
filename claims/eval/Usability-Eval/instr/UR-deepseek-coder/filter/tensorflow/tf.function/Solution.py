import tensorflow as tf

def compile_function_to_graph(func):
    # Define a TensorFlow graph
    graph = tf.Graph()
    
    with graph.as_default():
        # Convert the function to a TensorFlow graph
        func_graph = tf.function(func)
        
        # Create a callable TensorFlow function
        callable_func = func_graph.get_concrete_function()
    
    return callable_func

# Example usage
def example_function(x):
    return tf.square(x) + 2

compiled_function = compile_function_to_graph(example_function)

# Now you can call the compiled function with TensorFlow tensors
input_tensor = tf.constant(3.0)
output_tensor = compiled_function(input_tensor)

print(output_tensor.numpy())  # Output: 11.0
