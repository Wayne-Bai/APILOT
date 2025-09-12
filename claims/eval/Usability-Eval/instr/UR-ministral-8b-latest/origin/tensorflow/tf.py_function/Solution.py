import tensorflow as tf

def py_function(x):
    return x * 2

@tf.function
def create_op():
    return tf.py_function(py_function, [tf.constant(5)], tf.int32)

# Create the TF operation
op = create_op()

# Execute the TF operation
result = op()
print(result.numpy())  # Output should be 10
