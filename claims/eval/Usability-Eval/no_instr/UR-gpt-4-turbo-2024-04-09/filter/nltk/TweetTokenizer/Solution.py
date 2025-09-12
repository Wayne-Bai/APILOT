import nltk
from nltk.tokenize import TweetTokenizer

def tokenize_tweet(tweet):
    tokenizer = TweetTokenizer()
    return tokenizer.tokenize(tweet)

# Example usage
tweet = "This is a coool #dummysmiley: :-) :-P <3 and some arrows < > -> <--"
tokens = tokenize_tweet(tweet)
print(tokens)
