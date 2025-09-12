
import nltk
from nltk.tokenize import TweetTokenizer

# Create an instance of TweetTokenizer
tknzr = TweetTokenizer()

# Tokenize a sample tweet
text = "Hey @John, do you like #pizza?"
tokens = tknzr.tokenize(text)

print(tokens)  # Output: ['Hey', '@John', ',', 'do', 'you', 'like', '#pizza?']
