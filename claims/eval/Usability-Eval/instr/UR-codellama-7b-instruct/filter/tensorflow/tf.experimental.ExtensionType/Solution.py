import tensorflow as tf

class TensorFlowExtension(tf.Module):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._x = None

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value
