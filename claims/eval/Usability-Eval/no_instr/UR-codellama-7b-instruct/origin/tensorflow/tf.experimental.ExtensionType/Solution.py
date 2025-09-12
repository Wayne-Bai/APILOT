
from __future__ import absolute_import
import six

class TFExtensionType(six.with_metaclass(abc.ABCMeta)):
    """Base class for TensorFlow ExtensionType classes."""
    
    @abc.abstractmethod
    def to_tensor(self):
        """Converts the object into a Tensor."""
        raise NotImplementedError()
