
import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv("your_data.csv")

# Preprocess data
df = df.drop(columns=["target"])  # Drop target column
df = df.dropna()  # Drop any rows with missing values
X = df.iloc[:, :-1]  # Features
y = df.iloc[:, -1]  # Target

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize Random Forest Classifier with RFE
clf = RandomForestClassifier(n_jobs=-1, class_weight="balanced", random_state=42)
selector = RFE(estimator=clf, n_features_to_select=3)

# Perform recursive feature elimination with cross-validation
rfe_cv = selector.fit(X_train, y_train)
print("RFE CV Scores:", rfe_cv.scoring_)
print("RFE Importance Scores:", selector.support_)
