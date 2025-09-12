# Importing the required libraries
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import download
import string

# Download the required NLTK resources
download('punkt')
download('stopwords')

# Tokenizer function for tweets
def tweet_tokenizer(tweet):
    # Remove punctuation
    tweet = tweet.translate(str.maketrans('', '', string.punctuation))
    
    # Tokenize the tweet into words
    tokens = word_tokenize(tweet)
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word.lower() for word in tokens if word.isalpha() and word.lower() not in stop_words]
    
    return tokens

# Example usage
tweet = "I love #AI and Machine Learning. They're #awesome! # programming is fun."
print(tweet_tokenizer(tweet))
