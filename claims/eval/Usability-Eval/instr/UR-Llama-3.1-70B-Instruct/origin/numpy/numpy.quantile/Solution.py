import numpy as np

# Create a numpy array
data = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

# Define the axis and the q-th quantile value
axis = 0
q = 0.5  # This is the same as calculating the median

# Calculate the q-th quantile of the data along the specified axis
quantile = np.quantile(data, q, axis=axis)

print("Quantile for q =", q, "along axis", axis, ":", quantile)

# Calculate quantiles for multiple values of q
qs = [0.25, 0.5, 0.75]
quantiles = np.quantile(data, qs, axis=axis)

print("Quantiles for q =", qs, "along axis", axis, ":\n", quantiles)
