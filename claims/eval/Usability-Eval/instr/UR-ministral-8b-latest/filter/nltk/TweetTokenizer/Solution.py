import nltk
from nltk.tokenize import word_tokenize

# Download necessary NLTK data files
nltk.download('punkt')

# Sample tweet
tweet = "I love using Python for tweet processing! #NLTK rocks!"

# Tokenize the tweet
tokens = word_tokenize(tweet)

# Print the tokens
print(tokens)
