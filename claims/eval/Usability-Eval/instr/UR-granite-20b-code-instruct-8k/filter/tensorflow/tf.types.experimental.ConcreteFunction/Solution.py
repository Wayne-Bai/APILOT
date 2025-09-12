import tensorflow as tf
class MyLayer(tf.keras.layers.Layer):
  def __init__(self, units=32):
    super(MyLayer, self).__init__()
    self.units = units

  def build(self, input_shape):
    self.w = self.add_weight(
      shape=(input_shape[-1], self.units),
      initializer='random_normal',
      trainable=True
    )

  def call(self, inputs):
    return tf.matmul(inputs, self.w)
