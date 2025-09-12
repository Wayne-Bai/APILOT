import scipy.stats as stats

def calculate_coeff_variation(data):
    return (stats.variation(data))

# Test the function
data = [2, 8, 0, 4, 1, 7, 9]
print(calculate_coeff_variation(data))
