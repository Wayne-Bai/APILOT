
import torch
from torch import linalg as LA

def numerical_rank(matrix):
    return LA.matrix_rank(matrix)
