import tensorflow as tf

class AbstractOptimizer(object):
    """Abstract optimizer base class.
    Note: this is the parent class of all optimizers.
    """

    def __init__(self, use_locking, name):
        self._use_locking = use_locking
        self._name = name
        self._slots = {}
