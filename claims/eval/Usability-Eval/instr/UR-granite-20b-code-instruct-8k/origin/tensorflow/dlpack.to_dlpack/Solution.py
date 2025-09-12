
import tensorflow as tf

def generate_python_code(tensor):
  """
  Returns the dlpack capsule representing the tensor.
  """
  return tf.experimental.dlpack.to_dlpack(tensor)
