from rhodecode import Repository, Branch, Commit, File

# Create a new repository
repo = Repository.create("my_repository")

# Create a new branch
branch = repo.create_branch("my_branch")

# Create a new file on the branch
file = File.create(branch, "my_file.txt")
file.content = "Hello, World!"

# Create a new commit
commit = Commit.create(branch, "Initial commit")
commit.add_file(file)

# Update the commit message
commit.message = "Updated commit message"

# Commit the changes
commit.commit()

# Update the repository with the new commit
repo.update()
