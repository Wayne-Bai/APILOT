import rhodecode

def get_repository_by_name(name):
    try:
        repository = rhodecode.get_repository(name=name)
        return repository
    except rhodecode.RepositoryNotFound:
        print(f"Repository with name {name} not found.")
        return None

def get_repository_by_id(id):
    try:
        repository = rhodecode.get_repository(id=id)
        return repository
    except rhodecode.RepositoryNotFound:
        print(f"Repository with ID {id} not found.")
        return None

def get_repository_members(repository):
    members = repository.members
    return members
