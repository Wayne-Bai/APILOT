import rhodecode

repo = rhodecode.Repository(u'/path/to/repo')

# Make sure the working copy is up-to-date
repo.update()

# Create a new branch for our changes
new_branch = repo.branches.create(repo.branches.current.name, start_point=repo.commit.id)

# Update the file with the new information
repo.checkout(new_branch)
with open('file.txt', 'w') as f:
    f.write('New information here')
repo.add('file.txt')

# Commit our changes
repo.commit('Updated file with new information', author=' coding_expert < coding_expert@example.com>')

# Push our changes to the server
repo.push()
