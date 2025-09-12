import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import RFECV

# Load dataset
df = pd.read_csv("your_data.csv")

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df.drop("target", axis=1), df["target"], test_size=0.2, random_state=42)

# Initialize the model with recursive feature elimination
rfecv = RFECV(estimator=RandomForestClassifier(n_jobs=-1), step=1, cv=3)

# Fit the model and obtain the ranking of features
rfecv.fit(X_train, y_train)
ranking = rfecv.ranking_

# Print the ranking of features
print(ranking)
