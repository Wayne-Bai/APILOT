
import tensorflow as tf

@tf.function
def eager_function(py_function):
    @tf.function(experimental_compile=True)
    def eager_op(*args, **kwargs):
        return py_function(*args, **kwargs)

    return eager_op
