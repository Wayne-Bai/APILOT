import scipy.optimize

def global_minimum_function(func):
    result = scipy.optimize.minimize(func, 0)
    return result.x[0]

# Define your function here
def sample_function(x):
    return (x-2)**2

# Get the global minimum
min_value = global_minimum_function(sample_function)
print(f'Global minimum value: {min_value}')
