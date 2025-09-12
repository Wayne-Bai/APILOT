# Import necessary libraries
import nltk
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re

# Download required NLTK resources if not already downloaded
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

class TweetTokenizer:
    def __init__(self):
        self.tokenizer = TweetTokenizer()
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()

    def tokenize(self, tweet):
        # Remove URLs
        tweet = re.sub('http\S+', '', tweet)
        
        # Remove mentions
        tweet = re.sub('@\w+', '', tweet)
        
        # Remove hashtags
        tweet = re.sub('#\w+', '', tweet)
        
        # Tokenize the tweet
        tokens = self.tokenizer.tokenize(tweet)
        
        # Convert to lowercase
        tokens = [token.lower() for token in tokens]
        
        # Remove stopwords and punctuation
        tokens = [token for token in tokens if token.isalpha() and token not in self.stop_words]
        
        # Lemmatize tokens
        tokens = [self.lemmatizer.lemmatize(token) for token in tokens]
        
        return tokens

# Example usage
tokenizer = TweetTokenizer()
tweet = "This is a sample tweet with a URL https://www.example.com and a mention @user and a hashtag #hashtag"
print(tokenizer.tokenize(tweet))
