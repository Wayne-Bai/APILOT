
import numpy as np
from torch import Tensor

def tensor_to_numpy(tensor: Tensor) -> np.ndarray:
    """
    Convert a PyTorch tensor to a NumPy ndarray.

    Args:
        tensor (Tensor): The input PyTorch tensor.

    Returns:
        np.ndarray: The output NumPy ndarray.
    """
    return np.asarray(tensor.numpy())
