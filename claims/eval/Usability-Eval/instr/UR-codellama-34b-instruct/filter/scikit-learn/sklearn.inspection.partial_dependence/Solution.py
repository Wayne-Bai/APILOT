import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.inspection import partial_dependence

# Load data
df = pd.read_csv('data.csv')

# Create a gradient boosting regressor
gbr = GradientBoostingRegressor()

# Fit the model to the data
gbr.fit(df[['feature1', 'feature2']], df['target'])

# Extract the partial dependence of the first feature
pd_result = partial_dependence(gbr, df[['feature1']])

# Plot the partial dependence
plt.plot(pd_result)
