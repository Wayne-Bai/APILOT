
import nltk
from nltk.tokenize import TweetTokenizer

# Create a TweetTokenizer object
tknzr = TweetTokenizer()

# Tokenize a tweet
tweet = "This is a sample tweet! #NLP #tokenizer"
tokens = tknzr.tokenize(tweet)

print(tokens)
