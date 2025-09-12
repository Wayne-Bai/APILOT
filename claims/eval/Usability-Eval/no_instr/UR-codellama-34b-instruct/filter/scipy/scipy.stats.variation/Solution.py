from scipy.stats import variation

# Calculate the coefficient of variation for a dataset
data = [1, 2, 3, 4, 5]
coef_var = variation(data)
print("Coefficient of variation:", coef_var)
