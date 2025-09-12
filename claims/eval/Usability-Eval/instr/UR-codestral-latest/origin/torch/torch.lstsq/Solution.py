import torch

def solution_least_squares(A, b):
    # Compute the solution to the least squares problem using torch
    x = torch.linalg.lstsq(A, b).solution
    return x
