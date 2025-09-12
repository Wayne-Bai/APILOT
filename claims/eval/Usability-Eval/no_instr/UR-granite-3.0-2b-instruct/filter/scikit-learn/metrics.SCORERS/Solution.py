from sklearn.metrics import scorer

# Get the names of all available scorers
scorer_names = scorer.get_scorer_names()

# Print the names
for name in scorer_names:
    print(name)
