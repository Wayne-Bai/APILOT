import rhodecode

def update_repository(repo_slug, new_details):
    """
    Updates a repository with the given information using RhodeCode API.

    :param repo_slug: The slug or id of the repository to update.
    :param new_details: A dictionary containing the details to update.
    """
    client = rhodecode.RhodeCodeApiClient()
    response = client.update_repository(repo_id=repo_slug, **new_details)
    return response

# Example usage
repo_slug = 'example-repo'
new_details = {
    'description': 'Updated description of the repository.',
    'language': 'python'
}

response = update_repository(repo_slug, new_details)
print(response)
