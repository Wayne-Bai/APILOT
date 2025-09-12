import yaml

def load_yaml_file(file_path):
    """Load all documents from a YAML file."""
    with open(file_path, 'r') as file:
        # Load all documents within the YAML file
        documents = list(yaml.full_load_all(file))
    return documents

# Example usage:
# file_path = 'example.yaml'
# yaml_documents = load_yaml_file(file_path)
# for document in yaml_documents:
#     print(document)
