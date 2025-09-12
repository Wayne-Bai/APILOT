import nltk
from nltk.tokenize import TweetTokenizer

# Create a TweetTokenizer instance
tweet_tokenizer = TweetTokenizer()

# Example tweet
tweet = "Here's a sample tweet! #NLTK #Tokenization 😊"

# Tokenize the tweet
tokens = tweet_tokenizer.tokenize(tweet)

print(tokens)
