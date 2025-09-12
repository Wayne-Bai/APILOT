import sklearn.metrics

# Get the names of all available scorers
scorer_names = sorted(sklearn.metrics.get_scorer_names())

print(scorer_names)
