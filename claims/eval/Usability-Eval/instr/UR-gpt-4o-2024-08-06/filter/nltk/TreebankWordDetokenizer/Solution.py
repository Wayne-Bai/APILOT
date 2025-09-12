import nltk
from nltk.tokenize.treebank import TreebankWordTokenizer

# Define a custom Treebank Detokenizer
class TreebankWordDetokenizer:
    def __init__(self):
        self.regexes = [
            (r'\s+([.,!?;:])', r'\1'),
            (r'\s*((?<!\w)\')', r'\1'),
            (r'\b(can)\'\s*t\b', r"\1't"),
            (r'\b(Can)\'\s*t\b', r"\1't"),
            (r'\b(dam)\'\s*n\b', r"\1'n"),
            (r'\b(Dam)\'\s*n\b', r"\1'n"),
            (r'\s+(-)\s+', r'\1'),
            (r'\"(.+?)\s*\"', r'"\1"'),
            (r"(\s+'t)(?=\s)", r"'t"),
            (r'(\[.*?\]|\(.*?\)|\{.*?\})', r'\1'),
            (r'\b([A-Z])\s+\.\s+\b', r'\1.'),
            (r'\s+', r' ')
        ]
    
    def detokenize(self, tokens):
        text = ' '.join(tokens)
        for pattern, replace in self.regexes:
            text = nltk.re.sub(pattern, replace, text)
        return text.strip()

# Test case
tokenizer = TreebankWordTokenizer()
detokenizer = TreebankWordDetokenizer()

# Example tokenized sentence
tokens = tokenizer.tokenize("This is a test sentence. Isn't it great!")

# Detokenize
detokenized_text = detokenizer.detokenize(tokens)
print(detokenized_text)
