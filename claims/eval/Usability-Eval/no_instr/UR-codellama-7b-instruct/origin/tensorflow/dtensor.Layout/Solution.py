import tensorflow as tf

class DTensorLayout(object):
    def __init__(self, shape=None, dtype=tf.float32):
        self._shape = shape
        self._dtype = dtype
        
    @property
    def shape(self):
        return self._shape
    
    @property
    def dtype(self):
        return self._dtype
    
    def __repr__(self):
        return "DTensorLayout({}, {})".format(self.shape, self.dtype)
