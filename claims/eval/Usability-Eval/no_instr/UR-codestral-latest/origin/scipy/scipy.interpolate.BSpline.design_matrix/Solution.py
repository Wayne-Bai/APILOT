from scipy import sparse

# Let's assume these are your input data which will be converted to a design matrix
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Creating CSR format sparse array from the data
design_matrix = sparse.csr_matrix(data)

print(design_matrix)
