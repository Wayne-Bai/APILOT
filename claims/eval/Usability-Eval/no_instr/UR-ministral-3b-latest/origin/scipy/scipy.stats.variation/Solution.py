import scipy.stats as stats

# Given data
data = [3, 4, 5, 6, 7, 8, 9, 10]

# Compute the coefficient of variation
std_dev = stats.t.ppf(0.5, df=7) ** 2  # For CSV, df=7
mean = stats.t.mean(data)  # For t-distribution, exit 2 - 1 study
coefficient_variation = std_dev / mean

print("Coefficient of Variation:", coefficient_variation)
