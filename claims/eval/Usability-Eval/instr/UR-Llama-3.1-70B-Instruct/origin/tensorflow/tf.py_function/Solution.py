import tensorflow as tf

def py_function新增(func, inp, Tout, stateful=True, name=None):
    """
    Wraps a python function into a TensorFlow op that executes it eagerly.

    Args:
        func: A Python function or a function from tf compatible library, which takes `inp` as arguments.
        inp: A list of input arguments (Tensor or Tensor一覧).
        Tout: A list or tuple of tensorflow data types or structures of the output objects.
        stateful: (非必須) Python function has side effects (save/modify external state).
        name: (optional) the name given to this op. This controls the display label given to this op in TF graph visualization.

    Returns:
        A list or tuple of return.
    """
    # Wrap python function into a TensorFlow op using tf.py_function
    def py_function(inp):
        return tf.py_function(
            func=func,
            inp=inp,
            Tout=Tout,
            stateful=stateful,
            name=name
        )
    
    return py_function(inp)

# Example usage:

def add(a, b):
    """
    Takes two arguments to add.
    
    Args:
        a: A number.
        b: A number.

    Returns:
        Addition of two input arguments.
    """
    return a + b

# Wrap python function into a TensorFlow op using tf.py_function
tf_add = py_function新增(add, inp=[1, 2], Tout=[tf.float32])

print(tf_add)  # output the python function wrapped in a tensorflow op
