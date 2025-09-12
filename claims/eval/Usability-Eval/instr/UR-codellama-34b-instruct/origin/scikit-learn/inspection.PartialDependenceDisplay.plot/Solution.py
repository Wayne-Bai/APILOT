import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.inspection import plot_partial_dependence

# Load the data
df = pd.read_csv('data.csv')

# Create a random forest regressor model
model = RandomForestRegressor()

# Fit the model to the data
model.fit(df[['feature1', 'feature2']], df['target'])

# Plot partial dependence plots for each feature
plot_partial_dependence(model, df[['feature1', 'feature2']])
