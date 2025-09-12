import pandas as pd
from sklearn.feature_selection import RFE
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Load your dataset into a Pandas DataFrame
df = pd.read_csv('your_data.csv')

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df.drop('target', axis=1), df['target'], test_size=0.2)

# Initialize the linear regression model
model = LinearRegression()

# Perform feature ranking with recursive feature elimination
rfe = RFE(estimator=model, n_features_to_select=5)
rfe.fit(X_train, y_train)

# Print the ranking of features
print("Feature Ranking:")
for i, (feature, score) in enumerate(zip(df.columns[1:], rfe.ranking_)):
    print(f"{i+1}. {feature}: {score}")
