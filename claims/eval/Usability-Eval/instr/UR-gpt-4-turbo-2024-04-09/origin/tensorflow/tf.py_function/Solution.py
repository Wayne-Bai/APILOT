import tensorflow as tf

@tf.function
def wrapped_function(x):
    # Example Python function logic
    result = x + 42  # Arbitrary computation
    return result

# Test the function with TensorFlow
x_input = tf.constant(10)
output = wrapped_function(x_input)
print("Output:", output.numpy())
