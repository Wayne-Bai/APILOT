
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.corpora import brown_corpus
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

# Load the Brown corpus, which contains a large collection of text from various sources
brown_words = brown_corpus.words()

# Remove stop words from the text
stop_words = set(stopwords.words('english'))
brown_words = [word for word in brown_words if word not in stop_words]

# Tokenize the text into sentences
tokenizer = RegexpTokenizer(r'\.|\?|!')
sentences = tokenizer.tokenize(brown_words)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(sentences[:100], sentences[100:], test_size=0.2, random_state=42)

# Define a pipeline for the sentence tokenizer
pipeline = Pipeline([('tokenizer', RegexpTokenizer(r'\.|\?|!')), ('stop_words', stopwords.words('english')), ('logistic', LogisticRegression())])

# Train the pipeline on the training data
pipeline.fit(X_train, y_train)

# Use the trained model to predict the labels for the testing data
y_pred = pipeline.predict(X_test)

# Evaluate the performance of the model
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)
