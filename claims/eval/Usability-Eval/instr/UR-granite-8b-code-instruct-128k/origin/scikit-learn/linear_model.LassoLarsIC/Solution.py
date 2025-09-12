from sklearn.linear_model import LassoLars
from sklearn.metrics import make_scorer
from sklearn.model_selection import cross_val_score

# Load your data here
X = ...
y = ...

# Define your model
model = LassoLars()

# Define your scoring metric
scoring = make_scorer( scoring_function, greater_is_better=False )

# Perform cross-validation with BIC
scores_bic = cross_val_score( model, X, y, scoring='bic' )

# Perform cross-validation with AIC
scores_aic = cross_val_score( model, X, y, scoring='aic' )

# Print the results
print( 'BIC scores: {}'.format( scores_bic ) )
print( 'AIC scores: {}'.format( scores_aic ) )
