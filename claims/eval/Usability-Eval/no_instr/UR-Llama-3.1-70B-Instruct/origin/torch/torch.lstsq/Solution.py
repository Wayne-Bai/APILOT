import torch

# Define a function to solve least squares problem
def solve_least_squares(A, b):
    # A is a tensor of coefficients with shape (m, n)
    # b is a tensor of constants with shape (m)
    # Solve the least squares problem
    X = (A.T @ A).inverse() @ A.T @ b
    return X

# Example usage
if __name__ == "__main__":
    # Define the coefficients and the constant vector
    A = torch.tensor([[3, -6], [4, -8], [0, 1]])
    b = torch.tensor([5, 7, 2])

    # Solve the least squares problem
    X = solve_least_squares(A, b)
    
    # Print the solution
    print("Solution: ", X)

    # Alternatively, we can use the torch.linalg.lstsq function
    # to solve the least squares problem in a more stable way
    X_alt = torch.linalg.lstsq(A, b, driver='gelsd').solution
    print("Alternative solution: ", X_alt)
