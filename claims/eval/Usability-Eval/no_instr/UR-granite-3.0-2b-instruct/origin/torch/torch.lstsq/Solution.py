import torch

def compute_least_squares(A, b):
    # Compute the transpose of A
    A_t = A.t()

    # Compute the matrix product A_t * A
    A_t_mult_A = torch.matmul(A_t, A)

    # Compute the inverse of A_t * A
    inv_A_t_mult_A = torch.inverse(A_t_mult_A)

    # Compute the solution x by multiplying the inverse with A_t and b
    solution_x = torch.matmul(inv_A_t_mult_A, A_t)

    return solution_x
