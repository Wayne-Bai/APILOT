import nltk

def tokenize_tweet(tweet):
    tokens = nltk.word_tokenize(tweet)
    return tokens

tweet = "I love using nltk for tokenizing text data!"
print(tokenize_tweet(tweet))
