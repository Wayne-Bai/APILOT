
import tensorflow as tf

class TensorFlowExtensionType(tf.Tensor):
    def __init__(self, value):
        self._value = value

    @property
    def dtype(self):
        return self._value.dtype

    @property
    def shape(self):
        return self._value.shape

    def numpy(self):
        return self._value
