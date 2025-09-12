#!/bin/bash

# Function to clean files and repositories
clean_repo() {
    local path=$1

    # Check if path exists
    if [ -d "$path" ]; then
        # Remove all files in the directory
        find "$path" -type f -exec rm -f {} \;

        # Remove all subdirectories (repositories)
        find "$path" -mindepth 1 -type d -exec rm -rf {} \;

        echo "Cleanup complete in $path"
    else
        echo "Path $path does not exist."
    fi
}

# clean the ~/tests
clean_repo "$HOME/tests"
