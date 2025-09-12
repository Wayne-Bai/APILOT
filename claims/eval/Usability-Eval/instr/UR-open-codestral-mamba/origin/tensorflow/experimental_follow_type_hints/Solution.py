import tensorflow as tf
from tensorflow import Tensor

@tf.function
def my_func(arg: Tensor) -> Tensor:  # Adding the @tf.function decorator to optimize the performance
    # Your function logic here
    output = arg * 2  # Replace this with your specific logic
    return output
