import nltk
from nltk.tokenize import TweetTokenizer

# Initialize the TweetTokenizer
tweet_tokenizer = TweetTokenizer()

# Example tweet
tweet = "I love #python programming! It's awesome 😊 @OpenAI"

# Tokenize the tweet
tokens = tweet_tokenizer.tokenize(tweet)

# Print the tokens
print(tokens)
