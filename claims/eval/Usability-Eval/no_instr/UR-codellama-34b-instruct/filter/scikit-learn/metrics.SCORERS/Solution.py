
from sklearn.model_selection import cross_val_score

# get the names of all available scorers
scorer = cross_val_score(None, None, scoring="accuracy")
print(scorer.get_scorer_names())
