import scipy.stats as stats

def coefficient_of_variation(data):
    return stats.tstd(data) / stats.tmean(data)

# Use the function
data = [10, 20, 30, 40, 60]
coefficient = coefficient_of_variation(data)
print(f"The coefficient of variation for the data {data} is: {coefficient}")
