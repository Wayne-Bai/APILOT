import nltk
from nltk.tokenize import PunktSentenceTokenizer, word_tokenize

class CustomSentenceTokenizer:
    def __init__(self, text):
        self.text = text
        self.tokenizer = PunktSentenceTokenizer()
        
    def train_tokenizer(self):
        # Training the tokenizer on the given text
        self.tokenizer.train(self.text)
    
    def tokenize_sentences(self):
        # Tokenizing the sentences based on the trained model
        return self.tokenizer.tokenize(self.text)

# Example usage
if __name__ == "__main__":
    sample_text = """This is a sample text. It contains abbreviations, e.g., I.B.M. and Mr. Smith. 
                    It also includes various collocations. The weather is nice today! Let's enjoy."""
    
    sentence_tokenizer = CustomSentenceTokenizer(sample_text)
    sentence_tokenizer.train_tokenizer()
    sentences = sentence_tokenizer.tokenize_sentences()
    
    for sentence in sentences:
        print(sentence)
