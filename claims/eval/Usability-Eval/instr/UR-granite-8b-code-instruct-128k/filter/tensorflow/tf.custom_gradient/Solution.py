import tensorflow as tf

def custom_gradient(grad_fn):
  def wrapper(*args, **kwargs):
    with tf.GradientTape() as tape:
      tape.watch(*args)
      tape.watch(*kwargs.values())
      result = grad_fn(*args, **kwargs)
    grads = tape.gradient(result, (*args, *kwargs.values()))
    return result, grads
  return wrapper
