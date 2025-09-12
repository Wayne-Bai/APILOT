import nltk
from nltk.tokenize import TweetTokenizer

# Initialize the tokenizer
tknzr = TweetTokenizer()

# Tokenize a sample tweet
tweet = "This is an example tweet #hashtag with @mentions and https://www.example.com/links"
tokens = tknzr.tokenize(tweet)
print(tokens)
