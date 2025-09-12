
import pandas as pd
from sklearn.cross_decomposition import PLSRegression

# Load dataset
df = pd.read_csv('data.csv')

# Split data into input and output variables
X = df[['feature1', 'feature2']]
y = df['target']

# Perform Canonical Correlation Analysis (CCA)
cca = PLSRegression(n_components=1)
cca.fit(X, y)

# Print the loadings and scores for the first component
print('Loadings:')
print(cca.x_scores_)
print('Scores:')
print(cca.y_loadings_)
