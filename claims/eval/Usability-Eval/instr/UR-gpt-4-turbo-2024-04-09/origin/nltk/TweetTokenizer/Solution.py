import nltk
from nltk.tokenize import TweetTokenizer

# Initialize the tokenizer
tweet_tokenizer = TweetTokenizer()

# Example tweet
tweet = "This is a coool #dummysmiley: :-) :-P <3 and some arrows < > -> <--"

# Use the tokenizer
tokens = tweet_tokenizer.tokenize(tweet)

print(tokens)
