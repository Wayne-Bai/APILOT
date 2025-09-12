# Import scikit-learn's metrics module
from sklearn.metrics import get_scorer

# Get the names of all available scorers
scorers = get_scorer()

# Print the names of all available scorers
print(scorers)
