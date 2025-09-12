import nltk
import re

# Treebank detokenizer
class TreebankDetokenizer(nltk.tokenize.Tokenizer):
    def detokenize(self, tokens):
        text = ' '.join(tokens)
        # Contractions
        text = re.sub(r"``", r'"', text)
        text = re.sub(r"''", r'"', text)
        # Parentheses
        text = re.sub(r"\( ([^\)]+) \)", r"(\1)", text)
        text = text.replace(" -LRB- ", " (")
        text = text.replace(" -RRB- ", ") ")
        # Separate sentences
        text = re.sub(r'(?<=[.!?]) (?=[A-Z])', r'. ', text)
        # Handle decimals & number ranges
        text = re.sub(r' (\d+) \- (\d+)', r'\1-\2', text) # handle range
        text = re.sub(r' (\d+) \. (\d+)', r'\1.\2', text) # handle decimal
        return text

detokenizer = TreebankDetokenizer()

# Example usage:
tokens = ['This', 'is', 'an', 'example', '.', 'It', 'contains', 'other', 'tokens', '.']
detokenized_text = detokenizer.detokenize(tokens)
print(detokenized_text)
