import tensorflow as tf
import numpy as np

class ExtensionType(tf.ExtensionType):
    def __init__(self, device=None):
        super().__init__(device)
        self._trainable_variables = []
        self._non_trainable_variables = []

    @property
    def trainable_variables(self):
        return self._trainable_variables

    @property
    def non_trainable_variables(self):
        return self._non_trainable_variables

    def __call__(self, *args, **kwargs):
        raise NotImplementedError("This method must be overridden.")

    def call_with_dependencies(self, *args):
        """
        Execute the tensor computation with the given arguments. Allow to produce
        tensors and enumerate dependencies using TensorFlow operations.
        """
        raise NotImplementedError("This method must be overridden.")

    def _add_trainable_variable(self, var):
        if var.name not in [v.name for v in self.trainable_variables]:
            self._trainable_variables.append(var)

    def _add_non_trainable_variable(self, var):
        if var.name not in [v.name for v in self.non_trainable_variables]:
            self._non_trainable_variables.append(var)

    def _clear_variables(self):
        self._trainable_variables = []
        self._non_trainable_variables = []
