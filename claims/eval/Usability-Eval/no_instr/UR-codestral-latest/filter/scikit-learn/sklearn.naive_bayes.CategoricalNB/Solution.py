from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import CategoricalNB

# Initialize LabelEncoder
le = LabelEncoder()

# Assuming df is your DataFrame and the last column is the target
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

# Fit and transform all columns to numerical values
X = X.apply(le.fit_transform)

# Fit Naive Bayes classifier
clf = CategoricalNB()
clf.fit(X, y)
