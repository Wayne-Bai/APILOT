
import tensorflow as tf

class TensorFlowClassifier(tf.keras.models.Model):
  def __init__(self, units=1, activation='sigmoid', input_shape=(1,)):
    super(TensorFlowClassifier, self).__init__()
    self.dense1 = tf.keras.layers.Dense(units=units, activation=activation, input_shape=input_shape)
    self.output = tf.keras.layers.Dense(units=1, activation='sigmoid')

  def call(self, inputs):
    x = self.dense1(inputs)
    return self.output(x)
