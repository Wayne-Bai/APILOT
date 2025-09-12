import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

# Sample tweet for demonstration
tweet = "Python is an easy to learn, yet powerful language. It's also the most popular programming language in demand today."

# Tokenize the tweet using word_tokenize
word_tokens = word_tokenize(tweet)
print("Word Tokens:", word_tokens)

# Tokenize the tweet into sentences using sent_tokenize
sent_tokens = sent_tokenize(tweet)
print("Sentence Tokens:", sent_tokens)

# Download necessary NLTK data files if not already downloaded
nltk.download('punkt')
