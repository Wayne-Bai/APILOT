import scipy.stats as stats

def coefficient_of_variation(data):
    return stats.variation(data)

# sample usage
data = [1, 2, 3, 4, 5]
print(coefficient_of_variation(data))
