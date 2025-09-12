import tensorflow as tf

# Define a custom decorator to define a function with a custom gradient
def custom_gradient(func):
    def decorator(*args, **kwargs):
        with tf.GradientTape() as tape:
            outputs = func(*args, **kwargs)
            gradients = tape.gradient(outputs, kwargs.get('input_'))
            return outputs, gradients
    return decorator

# Define a custom function with custom gradient using the decorator
@custom_gradient
def custom_function(input_):
    # Define the custom function
    output = input_ ** 2
    return output

# Define the input
x = tf.Variable(2.0)

# Define the loss function
loss = custom_function(input_=x)[0]

# Apply the custom gradient
output, gradients = custom_function(input_=x)

# Print the output and gradients
print("Output:", output)
print("Gradients:", gradients)
