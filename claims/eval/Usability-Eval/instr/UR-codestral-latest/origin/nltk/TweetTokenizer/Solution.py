import nltk
from nltk.tokenize import TweetTokenizer

# Instantiate the tokenizer
tt = TweetTokenizer()

# A sample tweet
tweet = "This is a sample @Tweet with a #hashtag and some URLs https://www.example.com and another one http://example.org"

# Tokenize the tweet
tokens = tt.tokenize(tweet)

# Print the tokens
print(tokens)
