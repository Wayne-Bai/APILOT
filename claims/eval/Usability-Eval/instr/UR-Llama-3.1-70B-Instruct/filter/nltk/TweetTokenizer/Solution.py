import nltk
from nltk.tokenize import word_tokenize, sent_tokenize, TweetTokenizer
from string import punctuation
from nltk.corpus import stopwords

# Download required NLTK packages
nltk.download('punkt')
nltk.download('stopwords')

class TweetTokenizerImproved:
    def __init__(self):
        self.tt = TweetTokenizer()
        self.stop_words = set(stopwords.words('english'))

    def tokenize(self, tweet):
        # Tokenize the tweet
        tokens = self.tt.tokenize(tweet)
        
        # Remove punctuation and stopwords
        filtered_tokens = [t.lower() for t in tokens if t.isalpha() and t.lower() not in self.stop_words]
        
        return filtered_tokens

# Test the tokenizer
tweet = "This is a sample tweet with #hashtag and @username. I'm loving it! http://example.com"
tokenizer = TweetTokenizerImproved()

print(tokenizer.tokenize(tweet))
