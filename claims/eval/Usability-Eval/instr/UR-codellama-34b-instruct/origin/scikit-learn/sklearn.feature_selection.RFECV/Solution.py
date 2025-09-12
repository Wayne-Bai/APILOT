import pandas as pd
from sklearn.model_selection import train_test_split, KFold
from sklearn.feature_selection import RFECV
from sklearn.linear_model import LogisticRegression

# Load the data
df = pd.read_csv('data.csv')

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df.drop('target', axis=1), df['target'], test_size=0.2, random_state=42)

# Create a KFold object with 5 folds for cross-validation
kf = KFold(n_splits=5, shuffle=True, random_state=42)

# Perform recursive feature elimination with cross-validation
rfecv = RFECV(estimator=LogisticRegression(), cv=kf, scoring='accuracy')
rfecv.fit(X_train, y_train)

# Print the selected features and their corresponding scores
print("Selected Features:", rfecv.support_)
print("Feature Scores:", rfecv.ranking_)
