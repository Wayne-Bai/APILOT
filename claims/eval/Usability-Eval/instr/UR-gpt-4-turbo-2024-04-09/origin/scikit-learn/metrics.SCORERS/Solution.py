from sklearn.metrics import SCORERS

# Get all available scorers names
scorer_names = sorted(SCORERS.keys())

print("Available scorers in scikit-learn:")
print(scorer_names)
