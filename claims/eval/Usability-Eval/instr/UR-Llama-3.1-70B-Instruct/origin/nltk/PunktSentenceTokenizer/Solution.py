# Import required libraries
import nltk
import re
from nltk.tokenize import sent_tokenize, word_tokenize

# Ensure required NLTK resources are downloaded
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def sentence_tokenizer(text):
    """
    Tokenize input text into sentences.
    
    Parameters:
    text (str): The input text to be tokenized.
    
    Returns:
    list: A list of sentences.
    """
    
    # Regular expression pattern to match sentence-ending punctuation
    sentence_ending_punctuation = re.compile(r'(?<=[.!?])\s*')
    
    # Use regular expression to split text into sentences
    sentences = sentence_ending_punctuation.split(text)
    
    # Remove any empty strings from the list of sentences
    sentences = list(filter(None, sentences))
    
    return sentences

def word_tokenizer(sentence):
    """
    Tokenize input sentence into words.
    
    Parameters:
    sentence (str): The input sentence to be tokenized.
    
    Returns:
    list: A list of words.
    """
    
    # Use NLTK's word_tokenize function to split sentence into words
    words = word_tokenize(sentence)
    
    return words

def main():
    # Example usage
    text = "Mr. Smith is a great teacher. He teaches English. Mrs. Johnson is a nice person."
    
    # Tokenize text into sentences
    sentences = sentence_tokenizer(text)
    
    # Print sentences
    print("Sentences:")
    for i, sentence in enumerate(sentences):
        print(f"Sentence {i+1}: {sentence}")
        
        # Tokenize sentence into words
        words = word_tokenizer(sentence)
        
        # Print words
        print("Words:")
        for j, word in enumerate(words):
            print(f"Word {j+1}: {word}")
        
        print()

if __name__ == "__main__":
    main()
