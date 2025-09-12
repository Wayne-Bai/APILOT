import tensorflow as tf

@tf.function
def my_function(arg):
    if tf.is_tensor(arg):
        return arg * 2  # perform some operation for tensor
    else:
        return arg * 3  # perform some operation for non-tensor

# Test the function
print(my_function(tf.constant(5)))  # should print tf.Tensor(10, shape=(), dtype=int32)
print(my_function(7))  # should print 21
