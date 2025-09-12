# Import necessary library
from sklearn.metrics import get_scorer_names

def get_available_scorers():
    """
    Retrieves the names of all available scorers in scikit-learn.
    
    Returns:
        list: A list of available scorer names.
    """
    scorer_names = get_scorer_names()
    return scorer_names

# Example usage:
if __name__ == "__main__":
    available_scorers = get_available_scorers()
    print("Available Scorers:")
    for scorer in available_scorers:
        print(scorer)
