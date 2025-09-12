import tensorflow as tf

def wrap_as_tf_op(func):
    def wrapped_function(*args, **kwargs):
        with tf.GradientTape() as tape:
            tape.watch(*args, **kwargs)
            return func(*args, **kwargs)

    return tf.function(wrapped_function)

# Example of the usage
@wrap_as_tf_op
def add(a, b):
    return a + b

result = add(3, 5)
print(result)
