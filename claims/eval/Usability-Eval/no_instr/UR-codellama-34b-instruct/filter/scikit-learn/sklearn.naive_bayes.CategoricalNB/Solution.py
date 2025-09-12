import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# Load your dataset
df = pd.read_csv("your_data.csv")

# Encode categorical features using label encoding
label_encoder = LabelEncoder()
df[categorical_columns] = df[categorical_columns].apply(lambda x: label_encoder.fit_transform(x))

# Split your data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(df.drop("target", axis=1), df["target"], test_size=0.2, random_state=42)

# Create a Naive Bayes classifier for categorical features
nbc = MultinomialNB()
nbc.fit(X_train, y_train)

# Make predictions on the test set
y_pred = nbc.predict(X_test)

# Evaluate the performance of your model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
