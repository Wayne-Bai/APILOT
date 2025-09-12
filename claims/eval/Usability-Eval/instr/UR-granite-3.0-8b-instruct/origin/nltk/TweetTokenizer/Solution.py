import nltk
from nltk.tokenize import TweetTokenizer

# Download the punkt tokenizer for sentence tokenization
nltk.download('punkt')

# Initialize the TweetTokenizer
tokenizer = TweetTokenizer()

# Sample tweet
tweet = "Hello, this is a sample tweet! #NLP #Python"

# Tokenize the tweet
tokens = tokenizer.tokenize(tweet)

# Print the tokens
print(tokens)
