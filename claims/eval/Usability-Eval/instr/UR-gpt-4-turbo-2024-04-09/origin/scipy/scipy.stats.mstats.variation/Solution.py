import scipy.stats

def coefficient_of_variation(data):
    return scipy.stats.variation(data)

# Example usage with some data
data = [10, 12, 9, 11, 14]
print("Coefficient of Variation:", coefficient_of_variation(data))
