import nltk
from nltk.tokenize import TweetTokenizer

# Initialize the TweetTokenizer
tweet_tokenizer = TweetTokenizer()

# Example tweet
tweet = "Hello world! 😊 #NLP is awesome @user123"

# Tokenize the tweet
tokens = tweet_tokenizer.tokenize(tweet)

# Print the tokens
print(tokens)
