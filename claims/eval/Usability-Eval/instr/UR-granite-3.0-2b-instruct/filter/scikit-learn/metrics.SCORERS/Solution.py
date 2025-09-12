from sklearn.metrics import scoring

# Get the names of all available scorers
scorers = scoring.get_scorer().keys()

print(scorers)
