
import nltk
from nltk.tokenize import TweetTokenizer

tweet = "RT @JohnDoe: This is a sample tweet #SampleTweet"

tokenizer = TweetTokenizer()
tokens = tokenizer.tokenize(tweet)
print(tokens)
