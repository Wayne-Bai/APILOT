# Import the required libraries
from sklearn.metrics import SCORERS

# Get the names of all available scorers
sampler_scoring_functions = list(SCORERS.keys())

# Print the names of all available scorers
print(sampler_scoring_functions)
