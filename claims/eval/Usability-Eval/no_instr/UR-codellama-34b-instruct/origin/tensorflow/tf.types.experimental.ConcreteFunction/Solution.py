
import tensorflow as tf

@tf.function
def my_func(x):
    return x * x + x * x

# Use the `my_func` function to compute the output of a function that takes 
# an input and applies it to the `my_func` function
result = my_func(5)

# Print the output of the function
print(result)
