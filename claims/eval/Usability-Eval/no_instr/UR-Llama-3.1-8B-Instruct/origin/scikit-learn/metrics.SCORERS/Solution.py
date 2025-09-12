# Import necessary modules from scikit-learn
from sklearn.metrics import make_scorer

# Get the names of all available scorers
available_scorers = make_scorer().scorer_models.keys()

# Print the names of all available scorers
print("Available Scorers:")
for scorer in available_scorers:
    print(scorer)
