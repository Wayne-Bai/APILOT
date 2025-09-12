
from sklearn.feature_selection import SelectKBest
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load the data
df = pd.read_csv("data.csv")

# Preprocess the text data using TF-IDF vectorizer
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["text"])

# Select the top 50 most important features based on their importance weights
selector = SelectKBest(k=50)
X_selected = selector.fit_transform(X, df["label"])

# Create a multinomial Naive Bayes classifier and fit it to the selected data
clf = MultinomialNB()
clf.fit(X_selected, df["label"])
