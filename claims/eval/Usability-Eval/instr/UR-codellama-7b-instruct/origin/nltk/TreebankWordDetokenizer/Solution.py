import re
import nltk
from nltk.tokenize import TreebankWordDetokenizer

def detokenize(tokens):
    """
    Reverse operation of Treebank tokenizer's regexes.

    :param tokens: list of tokens to be detokenized
    :type tokens: list

    :return: the detokenized text
    :rtype: str
    """
    # Create a new instance of the TreebankWordDetokenizer
    detokenizer = TreebankWordDetokenizer()

    # Replace all special characters with their corresponding escape sequences
    tokens = [re.sub(r"([\.\?\!\:;\\])", r"\\\1", token) for token in tokens]

    # Remove any additional spaces that were inserted by the Treebank tokenizer
    tokens = [token.strip() for token in tokens]

    # Join all tokens into a single string using whitespace as the separator
    detokenized_text = " ".join(tokens)

    return detokenized_text

# Test the function with some examples
assert detokenize(["hello", "world"]) == "hello world"
assert detokenize(["hello", "world", "!"]) == "hello world !"
assert detokenize(["I", "'m", "happy"]) == "I 'm happy"
