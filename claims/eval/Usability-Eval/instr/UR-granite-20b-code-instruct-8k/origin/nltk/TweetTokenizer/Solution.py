import nltk
from nltk.tokenize import TweetTokenizer

# Initialize the TweetTokenizer
tokenizer = TweetTokenizer()

# Define the input tweet text
tweet_text = "This is an example tweet text."

# Tokenize the tweet text into separate words
tokenized_text = tokenizer.tokenize(tweet_text)

# Print the tokenized text
print(tokenized_text)
